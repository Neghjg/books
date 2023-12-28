from django import forms
from .models import Order
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django_recaptcha.fields import ReCaptchaField

# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name', 'address', 'email']
class NonAuthenticatedUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Имя", "id": "order_form"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Фамилия", "id": "order_form"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Адрес", "id": "order_form"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Адрес", "id": "order_form"}))
    recaptcha = ReCaptchaField()
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'email']

class AuthenticatedUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Имя", "id": "order_form"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Фамилия", "id": "order_form"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder" :"Адрес", "id": "order_form"}))
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address']
        