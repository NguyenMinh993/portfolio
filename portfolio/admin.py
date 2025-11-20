from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Experience, Photo, Skill
from .forms import ProjectForm, PhotoForm, ExperienceForm, SkillForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ['title', 'tech_stack', 'is_featured', 'order', 'image_preview', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description', 'tech_stack']
    list_editable = ['order', 'is_featured']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'tech_stack')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Image', {
            'fields': ('image_file', 'image_url'),
            'description': 'Upload a new image or use existing URL'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image_url)
        return "No image"
    image_preview.short_description = 'Preview'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceForm
    list_display = ['title', 'company', 'start_date', 'end_date', 'order']
    list_filter = ['company', 'start_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['order']
    ordering = ['order', '-start_date']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    form = PhotoForm
    list_display = ['title', 'category', 'is_featured', 'order', 'image_preview', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_featured']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Image', {
            'fields': ('image_file', 'image_url', 'thumbnail_url'),
            'description': 'Upload a new image or use existing URL'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image_url)
        return "No image"
    image_preview.short_description = 'Preview'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    form = SkillForm
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name', 'category']
    list_editable = ['order', 'proficiency']
    ordering = ['order', 'category']
