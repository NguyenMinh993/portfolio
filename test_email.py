import smtplib
from email.mime.text import MIMEText

# Test email credentials
EMAIL_HOST_USER = 'nguyenminh090903@gmail.com'
EMAIL_HOST_PASSWORD = 'nutcxgknxhvqeghb'  # App Password không có dấu cách

try:
    # Connect to Gmail SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    
    # Send test email
    msg = MIMEText('Test email from Django portfolio')
    msg['Subject'] = 'Test Email'
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = EMAIL_HOST_USER
    
    server.send_message(msg)
    server.quit()
    
    print("✅ Email sent successfully!")
    print("Credentials are correct!")
    
except smtplib.SMTPAuthenticationError as e:
    print("❌ Authentication failed!")
    print(f"Error: {e}")
    print("\nPlease check:")
    print("1. App Password is correct (no spaces)")
    print("2. 2-Step Verification is enabled")
    print("3. App Password is generated correctly")
    
except Exception as e:
    print(f"❌ Error: {e}")
