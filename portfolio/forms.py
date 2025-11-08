from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)
    source_page = forms.CharField(widget=forms.HiddenInput())
