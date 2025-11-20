from django import forms
from .models import Project, Photo, Experience, Skill
from .cloudinary_storage import get_cloudinary_storage


class ProjectForm(forms.ModelForm):
    """Form for creating/editing projects with image upload"""
    image_file = forms.ImageField(
        required=False,
        help_text="Upload image (will be stored in Cloudinary)"
    )
    
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_url', 'live_url', 
                  'image_url', 'order', 'is_featured']
        widgets = {
            'image_url': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'Auto-generated after upload'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make image_url not required if image_file is provided
        self.fields['image_url'].required = False
    
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
                raise forms.ValidationError(f"Failed to upload image: {str(e)}")
        elif not instance.image_url:
            raise forms.ValidationError("Please upload an image or provide an image URL")
        
        if commit:
            instance.save()
        return instance


class PhotoForm(forms.ModelForm):
    """Form for creating/editing photos with image upload"""
    image_file = forms.ImageField(
        required=False,
        help_text="Upload photo (will be stored in Cloudinary)"
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make image_url not required if image_file is provided
        self.fields['image_url'].required = False
        self.fields['thumbnail_url'].required = False
    
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
                raise forms.ValidationError(f"Failed to upload image: {str(e)}")
        elif not instance.image_url:
            raise forms.ValidationError("Please upload an image or provide an image URL")
        
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
