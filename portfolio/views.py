from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
import smtplib # Import smtplib to catch the specific error

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
            
            email_message = EmailMessage(
                subject,
                f'From: {user_email}\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                ['nguyenminh090903@gmail.com'],
                reply_to=[user_email],
            )

            if attachment:
                email_message.attach(attachment.name, attachment.read(), attachment.content_type)

            try:
                email_message.send()
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            except smtplib.SMTPAuthenticationError as e:
                # This is the specific error for bad username/password
                return JsonResponse({'success': False, 'message': 'SMTP Authentication Error: Please check your email credentials.', 'error_details': str(e)})
            except Exception as e:
                # Catch any other email-related errors
                return JsonResponse({'success': False, 'message': 'An error occurred while sending the email.', 'error_details': str(e)})
        else:
            # Form validation failed
            return JsonResponse({'success': False, 'message': 'Invalid form data. Please check the fields.', 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
