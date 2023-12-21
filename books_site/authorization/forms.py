from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', "id": "order_form"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', "id": "order_form"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "order_form"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "order_form"}))
    
    
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-control", "id": "order_form"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "order_form"}))
    
    

    