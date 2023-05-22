from django.forms import ModelForm
from django import forms
from .models import NewsLetter, Education, UserDetail

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

class AddEducation(ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'institute_name', 'marks']

        widgets={
                'name':forms.TextInput(attrs={'placeholder':'Enter course name','class':'form-control'}),
                'institute_name':forms.TextInput(attrs={'placeholder':'Enter school or college name','class':'form-control'}),
                'marks':forms.TextInput(attrs={'placeholder':'Enter grade in %','class':'form-control'}),
        }


class AddProfile(ModelForm):
    class Meta:
        model = UserDetail
        fields = ['name', 'gender', 'phone_number', 'country', 'state', 'city', 'address']

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter course name','class':'form-control'}),
            'gender':forms.RadioSelect(),
            'phone_number':forms.TextInput(attrs={'placeholder':'Enter phone number','class':'form-control'}),
            'country':forms.TextInput(attrs={'placeholder':'Enter country','class':'form-control'}),
            'state':forms.TextInput(attrs={'placeholder':'Enter state','class':'form-control'}),
            'city':forms.TextInput(attrs={'placeholder':'Enter city','class':'form-control'}),
            'address':forms.TextInput(attrs={'placeholder':'Enter address','class':'form-control'}),
        }