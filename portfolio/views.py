from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import ContactForm
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime

def health_check(request):
    """Simple health check endpoint"""
    return HttpResponse("OK", status=200)

def index(request):
    return render(request, 'portfolio/index.html')

@ensure_csrf_cookie
def photography(request):
    return render(request, 'portfolio/photography.html')

def contact_form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')
            source_page = form.cleaned_data['source_page']

            subject = f"New Contact: {source_page}"
            
            # Use Django SMTP with beautiful HTML template
            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Different themes based on source page
            if 'photo' in source_page.lower():
                theme_color = '#e74c3c'
                theme_gradient = 'linear-gradient(135deg, #e74c3c 0%, #c0392b 100%)'
                icon = '📸'
                title = 'New Photography Inquiry'
            else:
                theme_color = '#667eea'
                theme_gradient = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
                icon = '💼'
                title = 'New Job/Dev Inquiry'
            
            html_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 0; }}
                    .container {{ max-width: 600px; margin: 0 auto; background: white; }}
                    .header {{ background: {theme_color}; padding: 30px 20px; text-align: center; }}
                    .icon {{ font-size: 48px; margin-bottom: 10px; }}
                    .header h1 {{ color: white; font-size: 24px; font-weight: 700; margin: 0; }}
                    .content {{ padding: 20px; }}
                    .info-card {{ background: #f8f9fa; border-radius: 8px; padding: 15px; margin: 15px 0; }}
                    .info-row {{ padding: 10px 0; border-bottom: 1px solid #e9ecef; }}
                    .info-row:last-child {{ border-bottom: none; }}
                    .label {{ font-weight: 700; color: #2c3e50; font-size: 13px; margin-bottom: 5px; }}
                    .value {{ color: #7f8c8d; font-size: 14px; word-break: break-word; }}
                    .message-box {{ background: #fff5e6; padding: 20px; border-radius: 8px; border-left: 4px solid {theme_color}; margin: 20px 0; }}
                    .message-text {{ color: #2c3e50; font-size: 15px; line-height: 1.6; white-space: pre-wrap; word-wrap: break-word; }}
                    .button {{ display: inline-block; background: {theme_color}; color: white; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: 600; font-size: 14px; margin: 20px 0; }}
                    .footer {{ background: #2c3e50; padding: 20px; text-align: center; color: rgba(255,255,255,0.7); font-size: 12px; }}
                    @media only screen and (max-width: 600px) {{
                        .container {{ width: 100% !important; }}
                        .content {{ padding: 15px !important; }}
                        .header {{ padding: 20px 15px !important; }}
                        .header h1 {{ font-size: 20px !important; }}
                        .icon {{ font-size: 36px !important; }}
                        .message-box {{ padding: 15px !important; }}
                        .button {{ padding: 10px 25px !important; font-size: 13px !important; }}
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <div class="icon">{icon}</div>
                        <h1>{title}</h1>
                    </div>
                    <div class="content">
                        <div class="info-card">
                            <div class="info-row">
                                <div class="label">📧 From</div>
                                <div class="value">{user_email}</div>
                            </div>
                            <div class="info-row">
                                <div class="label">🕐 Time</div>
                                <div class="value">{current_time}</div>
                            </div>
                            <div class="info-row">
                                <div class="label">📍 Source</div>
                                <div class="value">{source_page}</div>
                            </div>
                        </div>
                        <div class="message-box">
                            <div class="label" style="margin-bottom: 10px;">💬 Message</div>
                            <div class="message-text">{message}</div>
                        </div>
                        <div style="text-align: center;">
                            <a href="mailto:{user_email}" class="button">Reply Now →</a>
                        </div>
                    </div>
                    <div class="footer">
                        <p>📧 Portfolio Contact Form</p>
                        <p style="margin-top: 10px;">© 2025 Nguyen Van Minh</p>
                    </div>
                </div>
            </body>
            </html>
                    .social-icons {{ margin: 20px 0; }}
                    .social-icons span {{ display: inline-block; margin: 0 8px; font-size: 20px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="top-banner">
                        <p>🎉 Celebrating you with something special! 🎉</p>
                    </div>
                    <div class="header">
                        <div class="icon-badge">{icon}</div>
                        <h1>{title}</h1>
                        <p>You have a new message waiting for you!</p>
                    </div>
                    <div class="content">
                        <div class="greeting">
                            <h2>Hello, Nguyen Van Minh! 👋</h2>
                            <p>Someone reached out to you from your portfolio</p>
                        </div>
                        
                        <div class="info-box">
                            <div class="info-row">
                                <span class="info-label">📧 From</span>
                                <span class="info-value">{user_email}</span>
                            </div>
                            <div class="info-row">
                                <span class="info-label">🕐 Time</span>
                                <span class="info-value">{current_time}</span>
                            </div>
                            <div class="info-row">
                                <span class="info-label">📍 Source</span>
                                <span class="info-value">{source_page}</span>
                            </div>
                        </div>
                        
                        <div class="message-section">
                            <div class="message-label">💬 Message Content</div>
                            <div class="message-box">{message}</div>
                        </div>
                        
                        <div class="cta-section">
                            <p style="margin: 0 0 15px; color: #7f8c8d; font-size: 14px;">Ready to respond?</p>
                            <a href="mailto:{user_email}" class="cta-button">Reply Now →</a>
                        </div>
                    </div>
                    <div class="footer">
                        <div class="footer-logo">Nguyen Van Minh</div>
                        <div class="footer-links">
                            <a href="https://nguyenminh993.up.railway.app">Portfolio</a>
                            <a href="https://github.com/NguyenMinh993">GitHub</a>
                            <a href="https://www.linkedin.com/in/văn-minh-nguyễn">LinkedIn</a>
                        </div>
                        <div class="social-icons">
                            <span>📘</span>
                            <span>📷</span>
                            <span>🐦</span>
                            <span>💼</span>
                        </div>
                        <p>📧 Sent via Portfolio Contact Form</p>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.5); margin-top: 15px;">
                            © 2025 Nguyen Van Minh | Full Stack Developer
                        </p>
                    </div>
                </div>
            </body>
            </html>
            '''
            
            # Create plain text version for better deliverability
            plain_text = f"""
New Contact from Portfolio

From: {user_email}
Time: {current_time}
Source: {source_page}

Message:
{message}

---
Reply to: {user_email}
            """
            
            # Simple SendGrid email - no complex features
            try:
                api_key = os.environ.get('SENDGRID_API_KEY')
                
                if not api_key or api_key == 'YOUR_SENDGRID_API_KEY_HERE':
                    raise Exception("SendGrid API key not configured")
                
                # Create simple email message
                message = Mail(
                    from_email='nguyenminh090903@gmail.com',
                    to_emails='nguyenminh090903@gmail.com',
                    subject=subject,
                    html_content=html_content
                )
                
                # Send via SendGrid
                sg = SendGridAPIClient(api_key)
                response = sg.send(message)
                
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
                
            except Exception as e:
                import traceback
                return JsonResponse({
                    'success': False, 
                    'message': 'Failed to send email. Please try again later.', 
                    'error': str(e),
                    'error_type': type(e).__name__,
                    'traceback': traceback.format_exc()
                })
        else:
            # Form validation failed
            return JsonResponse({'success': False, 'message': 'Invalid form data. Please check the fields.', 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
