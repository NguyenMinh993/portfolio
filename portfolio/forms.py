from django import forms
from .models import Project, Photo, Experience, Skill
from .azure_storage import get_azure_storage


class ProjectForm(forms.ModelForm):
    """Form for creating/editing projects with image upload"""
    image_file = forms.ImageField(
        required=False,
        help_text="Upload image (will be stored in Azure Blob Storage)"
    )
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_url', 'live_url', 
                  'image_url', 'order', 'is_featured']
        widgets = {
            'image_url': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'Auto-generated after upload'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Upload image to Azure if provided
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            try:
                azure_storage = get_azure_storage()
                image_url = azure_storage.upload_image(image_file)
                instance.image_url = image_url
            except Exception as e:
                raise forms.ValidationError(f"Failed to upload image: {str(e)}")
        
        if commit:
            instance.save()
        return instance


class PhotoForm(forms.ModelForm):
    """Form for creating/editing photos with image upload"""
    image_file = forms.ImageField(
        required=False,
        help_text="Upload photo (will be stored in Azure Blob Storage)"
    )
    
    class Meta:
        model = Photo
        fields = ['title', 'description', 'category', 'image_url', 'thumbnail_url',
                  'order', 'is_featured']
        widgets = {
            'image_url': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'Auto-generated after upload'}),
            'thumbnail_url': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'Optional'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Upload image to Azure if provided
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            try:
                azure_storage = get_azure_storage()
                image_url = azure_storage.upload_image(image_file)
                instance.image_url = image_url
                # You can also generate thumbnail here if needed
            except Exception as e:
                raise forms.ValidationError(f"Failed to upload image: {str(e)}")
        
        if commit:
            instance.save()
        return instance


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'proficiency': forms.NumberInput(attrs={'min': 0, 'max': 100}),
        }
