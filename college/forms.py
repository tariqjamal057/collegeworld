from django.forms import ModelForm
from django import forms
from .models import NewsLetter

class NewsLetterForm(ModelForm):
     
    email = forms.EmailField(
        label = 'Email address',
        widget = forms.EmailInput(attrs={'class': 'form-control me-2', 'placeholder': 'Enter email address', 'type': 'email', 'name': 'email'})
    )

    class Meta:
        model = NewsLetter
        fields = ['name', 'email', 'course']

        widgets={
                'name':forms.TextInput(attrs={'placeholder':'Enter Name','class':'form-control me-2'}),
                'course': forms.Select(attrs={'class': 'form-select select2-dropown me-2'})
        }