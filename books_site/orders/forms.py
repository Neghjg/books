from django import forms
from .models import Order
from django_recaptcha.fields import ReCaptchaField


class NonAuthenticatedUserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    requires_delivery = forms.ChoiceField(choices=[("0", False), ("1", True)])
    address = forms.CharField(required=False)
    email = forms.EmailField()
    payment_on_get = forms.ChoiceField(choices=[("0", False), ("1", True)])
    recaptcha = ReCaptchaField()
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'requires_delivery', 'address', 'email', 'payment_on_get']

class AuthenticatedUserForm(forms.ModelForm):
    #first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "order_form", "placeholder" :"Имя"}))
    #last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "order_form", "placeholder" :"Фамилия"}))
    #requires_delivery = forms.ChoiceField(widget=forms.RadioSelect(choices=[("0", False), ("1", True)], attrs={"class": "form-check-input"})) 
    #address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "order_form", "placeholder" :"Адрес"}))
    #payment_on_get = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class": "form-check-input", "placeholder" :"Оплата при получении"}))
    
    requires_delivery = forms.ChoiceField(choices=[
            ("0", False),
            ("1", True),
            ],) 
    address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(choices=[
            ("0", False),
            ("1", True),
            ],)
    
    class Meta:
        model = Order
        fields = ['requires_delivery', 'address', 'payment_on_get']
        