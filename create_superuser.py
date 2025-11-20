#!/usr/bin/env python
"""
Script to create superuser automatically
Run: python create_superuser.py
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
django.setup()

from django.contrib.auth import get_user_model

try:
    User = get_user_model()
    
    username = 'admin'
    email = 'nguyenminh090903@gmail.com'
    password = 'Admin@123456'  # Change this!
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f'✅ Superuser "{username}" created successfully!')
    else:
        print(f'⚠️  Superuser "{username}" already exists.')
    
    sys.exit(0)  # Exit successfully
    
except Exception as e:
    print(f'❌ Error creating superuser: {e}')
    sys.exit(0)  # Don't fail deployment
