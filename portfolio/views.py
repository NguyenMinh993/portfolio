from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .forms import ContactForm
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64

def health_check(request):
    """Simple health check endpoint"""
    return HttpResponse("OK", status=200)

def index(request):
    return render(request, 'portfolio/index.html')

def photography(request):
    from .models import Photo
    
    # Get photos from database
    digital_photos = Photo.objects.filter(category='digital', is_featured=True).order_by('order', '-created_at')[:6]
    film_photos = Photo.objects.filter(category='film', is_featured=True).order_by('order', '-created_at')[:6]
    all_photos = Photo.objects.filter(is_featured=True).order_by('order', '-created_at')[:12]
    
    context = {
        'digital_photos': digital_photos,
        'film_photos': film_photos,
        'all_photos': all_photos,
    }
    
    return render(request, 'portfolio/photography.html', context)

def contact_form_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')
            source_page = form.cleaned_data['source_page']

            subject = f"New Contact: {source_page}"
            
            # Use SendGrid API with beautiful HTML template
            import datetime
            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Different images based on source page
            if 'photo' in source_page.lower():
                hero_image = 'https://picsum.photos/600/400?random=1'
                theme_color = '#e74c3c'
                theme_gradient = 'linear-gradient(135deg, #e74c3c 0%, #c0392b 100%)'
                icon = '📸'
                title = 'New Photography Inquiry'
            else:
                hero_image = 'https://picsum.photos/600/400?random=2'
                theme_color = '#667eea'
                theme_gradient = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
                icon = '💼'
                title = 'New Job/Dev Inquiry'
            
            html_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #fef6e4; margin: 0; padding: 20px; }}
                    .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 40px rgba(0,0,0,0.15); border: 3px solid #f3d250; }}
                    .top-banner {{ background: {theme_gradient}; padding: 20px; text-align: center; }}
                    .top-banner p {{ color: white; margin: 0; font-size: 14px; font-weight: 600; }}
                    .header {{ background: linear-gradient(180deg, #fff 0%, #f8f9fa 100%); padding: 40px 30px 20px; text-align: center; }}
                    .icon-badge {{ font-size: 48px; margin-bottom: 15px; }}
                    .header h1 {{ color: #2c3e50; margin: 0; font-size: 36px; font-weight: 800; line-height: 1.2; }}
                    .header p {{ color: #7f8c8d; margin: 12px 0 0; font-size: 16px; }}
                    .hero-image {{ width: 100%; height: 300px; object-fit: cover; display: block; }}
                    .content {{ padding: 35px 30px; }}
                    .greeting {{ background: {theme_gradient}; color: white; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 30px; }}
                    .greeting h2 {{ margin: 0 0 8px; font-size: 22px; }}
                    .greeting p {{ margin: 0; font-size: 14px; opacity: 0.95; }}
                    .info-box {{ background: #f8f9fa; border-radius: 12px; padding: 20px; margin-bottom: 25px; border-left: 5px solid {theme_color}; }}
                    .info-row {{ display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #e9ecef; }}
                    .info-row:last-child {{ border-bottom: none; }}
                    .info-label {{ font-weight: 700; color: #2c3e50; font-size: 14px; }}
                    .info-value {{ color: #7f8c8d; font-size: 14px; text-align: right; }}
                    .message-section {{ margin: 30px 0; }}
                    .message-label {{ font-size: 14px; font-weight: 700; color: {theme_color}; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }}
                    .message-box {{ background: linear-gradient(135deg, #fff5e6 0%, #ffe6cc 100%); padding: 25px; border-radius: 12px; border: 2px dashed {theme_color}; white-space: pre-wrap; font-size: 16px; line-height: 1.8; color: #2c3e50; min-height: 100px; }}
                    .cta-section {{ text-align: center; margin: 35px 0; padding: 30px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 12px; }}
                    .cta-button {{ display: inline-block; background: {theme_gradient}; color: white; padding: 15px 40px; border-radius: 30px; text-decoration: none; font-weight: 700; font-size: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
                    .footer {{ background: #2c3e50; padding: 30px; text-align: center; }}
                    .footer-logo {{ color: white; font-size: 24px; font-weight: 800; margin-bottom: 15px; }}
                    .footer-links {{ margin: 20px 0; }}
                    .footer-links a {{ color: {theme_color}; text-decoration: none; margin: 0 15px; font-size: 14px; font-weight: 600; }}
                    .footer p {{ color: rgba(255,255,255,0.7); font-size: 13px; margin: 8px 0; }}
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
                    <img src="{hero_image}" alt="Hero" class="hero-image">
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
            
            message_obj = Mail(
                from_email=os.environ.get('FROM_EMAIL', 'nguyenminh090903@gmail.com'),
                to_emails='nguyenminh090903@gmail.com',
                subject=subject,
                html_content=html_content
            )
            
            # Add attachment if present
            if attachment:
                file_content = base64.b64encode(attachment.read()).decode()
                attached_file = Attachment(
                    FileContent(file_content),
                    FileName(attachment.name),
                    FileType(attachment.content_type),
                    Disposition('attachment')
                )
                message_obj.attachment = attached_file

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message_obj)
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            except Exception as e:
                import traceback
                return JsonResponse({
                    'success': False, 
                    'message': 'Email Error', 
                    'error': str(e),
                    'error_type': type(e).__name__,
                    'traceback': traceback.format_exc()
                })
        else:
            # Form validation failed
            return JsonResponse({'success': False, 'message': 'Invalid form data. Please check the fields.', 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
