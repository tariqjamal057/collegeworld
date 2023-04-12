from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(
        label = 'Email address', 
        widget = forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Enter email address', 'class': 'form-control my-1', 'id': 'email'})
    )
    password1 = forms.CharField(
        label = 'Password',
        widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Enter password', 'class': 'form-control my-1', 'id': 'password', 'minlength': 5, 'maxlength': 15}),
    )
    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Re-enter password', 'class': 'form-control my-1', 'id': 'password2'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'form-control my-1', 'id': 'username', 'minlength': 3, 'maxlength': 15,'aria-describedby':'basic-addon1', 'autofocus': True}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        username = username.lower()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already taken. Please choose a different one.')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        email = email.lower()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already taken. Please choose a different one.')


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        label = 'Email address',
        widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address', 'type': 'email', 'name': 'email'})
    )


class SetPasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('old_password', None)


    new_password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Enter password', 'class': 'form-control my-2', 'id': 'password','name': 'new_password1'}),
    )
    new_password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Re-enter passwordd', 'class': 'form-control my-2', 'id': 'password2','name': 'new_password2'}),
    )
