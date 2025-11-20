from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(help_text="Cloudinary image URL")
    order = models.IntegerField(default=0, help_text="Display order")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    """Model for work experience"""
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=500)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if current")
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Photo(models.Model):
    """Model for photography portfolio"""
    CATEGORY_CHOICES = [
        ('digital', 'Digital Photography'),
        ('film', 'Film Photography'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='digital')
    image_url = models.URLField(help_text="Cloudinary image URL")
    thumbnail_url = models.URLField(blank=True, help_text="Cloudinary thumbnail URL")
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Model for skills"""
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, help_text="e.g., Frontend, Backend, Database")
    proficiency = models.IntegerField(default=50, help_text="0-100")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"
