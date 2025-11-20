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
            html_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f5f5f5; margin: 0; padding: 20px; }}
                    .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
                    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center; }}
                    .header h1 {{ color: white; margin: 0; font-size: 28px; font-weight: 600; }}
                    .header p {{ color: rgba(255,255,255,0.9); margin: 10px 0 0; font-size: 14px; }}
                    .content {{ padding: 40px 30px; }}
                    .field {{ margin-bottom: 25px; }}
                    .label {{ color: #667eea; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }}
                    .value {{ color: #333; font-size: 16px; line-height: 1.6; background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #667eea; }}
                    .message-box {{ background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #764ba2; white-space: pre-wrap; }}
                    .footer {{ background: #f8f9fa; padding: 20px 30px; text-align: center; border-top: 1px solid #e0e0e0; }}
                    .footer p {{ color: #666; font-size: 13px; margin: 5px 0; }}
                    .badge {{ display: inline-block; background: #667eea; color: white; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-top: 10px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>📬 New Contact Message</h1>
                        <p>You have received a new message from your portfolio</p>
                        <span class="badge">{source_page}</span>
                    </div>
                    <div class="content">
                        <div class="field">
                            <div class="label">👤 From</div>
                            <div class="value">{user_email}</div>
                        </div>
                        <div class="field">
                            <div class="label">💬 Message</div>
                            <div class="message-box">{message}</div>
                        </div>
                    </div>
                    <div class="footer">
                        <p>📧 Sent via Portfolio Contact Form</p>
                        <p>🌐 <a href="https://nguyenminh993.up.railway.app" style="color: #667eea; text-decoration: none;">nguyenminh993.up.railway.app</a></p>
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
