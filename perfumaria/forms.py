from django.contrib.auth.models import User
 
# forms.py
from django import forms
from django.core.exceptions import ValidationError
import re
 
 
class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
 
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()
 
        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )
 
        return email
 
    def validate_complex_password(value):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', value):
            raise ValidationError(
                "A senha deve conter uma letra maiúscula, uma letra minúscula e um número.")
 
    password = forms.CharField(widget=forms.PasswordInput(), validators=[
                               validate_complex_password])
    

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    password = forms.CharField(
            label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
                   