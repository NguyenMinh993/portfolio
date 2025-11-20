from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .forms import ContactForm
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64

def index(request):
    return render(request, 'portfolio/index.html')

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
            
            # Use SendGrid API with beautiful HTML template
            import datetime
            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            html_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }}
                    .container {{ max-width: 650px; margin: 0 auto; background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.12); }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 40px; text-align: center; position: relative; }}
                    .header::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="rgba(255,255,255,0.1)"/></svg>'); opacity: 0.1; }}
                    .header h1 {{ color: white; margin: 0; font-size: 32px; font-weight: 700; position: relative; }}
                    .header p {{ color: rgba(255,255,255,0.95); margin: 15px 0 0; font-size: 16px; position: relative; }}
                    .badge {{ display: inline-block; background: rgba(255,255,255,0.25); color: white; padding: 8px 16px; border-radius: 25px; font-size: 13px; font-weight: 600; margin-top: 15px; backdrop-filter: blur(10px); }}
                    .content {{ padding: 45px 40px; }}
                    .info-grid {{ display: table; width: 100%; margin-bottom: 30px; }}
                    .info-row {{ display: table-row; }}
                    .info-label {{ display: table-cell; color: #667eea; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; padding: 12px 20px 12px 0; vertical-align: top; width: 140px; }}
                    .info-value {{ display: table-cell; color: #333; font-size: 16px; padding: 12px 0; }}
                    .field {{ margin-bottom: 30px; }}
                    .label {{ color: #667eea; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }}
                    .value {{ color: #333; font-size: 16px; line-height: 1.6; background: #f8f9fa; padding: 18px 20px; border-radius: 10px; border-left: 5px solid #667eea; }}
                    .message-box {{ background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 25px; border-radius: 12px; border-left: 5px solid #764ba2; white-space: pre-wrap; font-size: 16px; line-height: 1.8; color: #2c3e50; min-height: 80px; }}
                    .stats {{ display: flex; justify-content: space-around; background: #f8f9fa; padding: 25px; border-radius: 12px; margin-top: 30px; }}
                    .stat-item {{ text-align: center; }}
                    .stat-value {{ font-size: 24px; font-weight: 700; color: #667eea; }}
                    .stat-label {{ font-size: 12px; color: #666; margin-top: 5px; text-transform: uppercase; letter-spacing: 1px; }}
                    .footer {{ background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); padding: 30px 40px; text-align: center; }}
                    .footer p {{ color: rgba(255,255,255,0.8); font-size: 14px; margin: 8px 0; }}
                    .footer a {{ color: #667eea; text-decoration: none; font-weight: 600; }}
                    .footer a:hover {{ color: #764ba2; }}
                    .action-btn {{ display: inline-block; background: #667eea; color: white; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: 600; margin-top: 15px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>📬 New Contact Message</h1>
                        <p>You have received a new message from your portfolio website</p>
                        <span class="badge">🏷️ {source_page}</span>
                    </div>
                    <div class="content">
                        <div class="info-grid">
                            <div class="info-row">
                                <div class="info-label">📧 EMAIL</div>
                                <div class="info-value"><strong>{user_email}</strong></div>
                            </div>
                            <div class="info-row">
                                <div class="info-label">🕐 TIME</div>
                                <div class="info-value">{current_time}</div>
                            </div>
                            <div class="info-row">
                                <div class="info-label">📍 SOURCE</div>
                                <div class="info-value">{source_page}</div>
                            </div>
                        </div>
                        
                        <div class="field">
                            <div class="label">💬 MESSAGE CONTENT</div>
                            <div class="message-box">{message}</div>
                        </div>
                        
                        <div class="stats">
                            <div class="stat-item">
                                <div class="stat-value">📨</div>
                                <div class="stat-label">New Message</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">✅</div>
                                <div class="stat-label">Delivered</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">🚀</div>
                                <div class="stat-label">Action Required</div>
                            </div>
                        </div>
                    </div>
                    <div class="footer">
                        <p>📧 Sent via Portfolio Contact Form</p>
                        <p>🌐 <a href="https://nguyenminh993.up.railway.app">nguyenminh993.up.railway.app</a></p>
                        <p style="font-size: 12px; color: rgba(255,255,255,0.6); margin-top: 15px;">
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
