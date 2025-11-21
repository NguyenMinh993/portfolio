#!/usr/bin/env python3
"""
Test SendGrid API Key
Run: python test_sendgrid.py
"""
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Get API key from environment
api_key = os.environ.get('SENDGRID_API_KEY')

if not api_key:
    print("❌ SENDGRID_API_KEY not found in environment variables")
    print("Set it in Railway Dashboard → Variables")
    exit(1)

print(f"✓ Found API key: {api_key[:10]}...")

# Test sending a simple email
message = Mail(
    from_email='nguyenminh090903@gmail.com',
    to_emails='nguyenminh090903@gmail.com',
    subject='SendGrid Test',
    html_content='<strong>This is a test email from SendGrid</strong>'
)

try:
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    print(f"✓ Email sent successfully!")
    print(f"  Status code: {response.status_code}")
    print(f"  Response body: {response.body}")
    print(f"  Response headers: {response.headers}")
except Exception as e:
    print(f"❌ Failed to send email:")
    print(f"  Error: {e}")
    print(f"  Type: {type(e).__name__}")
