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
            
            # Use SendGrid API instead of SMTP
            message_obj = Mail(
                from_email=os.environ.get('FROM_EMAIL', 'nguyenminh090903@gmail.com'),
                to_emails='nguyenminh090903@gmail.com',
                subject=subject,
                html_content=f'<p><strong>From:</strong> {user_email}</p><p><strong>Message:</strong></p><p>{message}</p>'
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
