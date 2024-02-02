from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField


class RegistrationUserForm(UserCreationForm):
    #backend
    #username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', "id": "order_form"}))
    #email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', "id": "order_form"}))
    #password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "order_form"}))
    #password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "order_form"}))
    #recaptcha = ReCaptchaField()
    
    # Frontend
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    recaptcha = ReCaptchaField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже зарегистрирован.")
        return email
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        
    
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-control", "id": "order_form"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", "id": "order_form"}))
    
    
class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                "id": "order_form",
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                "id": "order_form",
                'autocomplete': 'off'
            })


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()