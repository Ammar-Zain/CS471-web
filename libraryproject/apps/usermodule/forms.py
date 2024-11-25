from django import forms
from django.contrib.auth.models import User

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    username = forms.CharField(max_length=50, required=True, label="username")
    email = forms.EmailField(max_length=50, required=True, label="email")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="password")

class UserLogin(forms.Form):
    username = forms.CharField(max_length=50, required=True, label="username")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="password")