from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # No need to redefine email
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }
