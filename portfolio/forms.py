from django import forms
from .models import Project, Photo, Experience, Skill
from .cloudinary_storage import get_cloudinary_storage


class ProjectForm(forms.ModelForm):
    """Form for creating/editing projects with image upload"""
    image_file = forms.ImageField(
        required=False,
        help_text="Upload new image (will be stored in Cloudinary)"
    )
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_url', 'live_url', 
                  'order', 'is_featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        image_file = cleaned_data.get('image_file')
        
        # For new records, require image
        if not self.instance.pk and not image_file:
            raise forms.ValidationError("Please upload an image for new project")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Upload image to Cloudinary if provided
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            try:
                cloudinary_storage = get_cloudinary_storage()
                image_url = cloudinary_storage.upload_image(image_file, folder='projects')
                instance.image_url = image_url
            except Exception as e:
                import traceback
                error_detail = traceback.format_exc()
                print(f"❌ Cloudinary upload error: {error_detail}")
                raise forms.ValidationError(f"Failed to upload image: {str(e)}")
        
        if commit:
            instance.save()
        return instance


class PhotoForm(forms.ModelForm):
    """Form for creating/editing photos with image upload"""
    image_file = forms.ImageField(
        required=False,
        help_text="Upload new photo (will be stored in Cloudinary)"
    )
    
    class Meta:
        model = Photo
        fields = ['title', 'description', 'category', 'order', 'is_featured']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        image_file = cleaned_data.get('image_file')
        
        # For new records, require image
        if not self.instance.pk and not image_file:
            raise forms.ValidationError("Please upload an image for new photo")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Upload image to Cloudinary if provided
        image_file = self.cleaned_data.get('image_file')
        if image_file:
            try:
                cloudinary_storage = get_cloudinary_storage()
                result = cloudinary_storage.upload_photo(image_file, folder='photos')
                instance.image_url = result['image_url']
                instance.thumbnail_url = result['thumbnail_url']
            except Exception as e:
                import traceback
                error_detail = traceback.format_exc()
                print(f"❌ Cloudinary upload error: {error_detail}")
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


class ContactForm(forms.Form):
    """Form for contact page"""
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    attachment = forms.FileField(required=False)
