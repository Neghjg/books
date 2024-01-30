from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from orders.models import Order, OrderItem
from django.db.models import Prefetch
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForgotPasswordForm, UserSetNewPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login_user(request, user)
            messages.success(request, f'{username}, Вы успешно зарегестрированны и вошли в аккаунт')
            return redirect('/')
    else:
        form = RegistrationUserForm()
    return render(request, 'authorization/registration.html', {'form': form, 'title': 'Bookingcom - Регистрация'})


def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                messages.success(request, f'{username}, Вы успешно вошли в аккаунт')
                return redirect('/')
    else:
        form = LoginUserForm()
    return render(request, 'authorization/login.html', {'form': form, 'title': 'Bookingcom - Авторизация'})

def logout_user(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта')
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = OrderItem.objects.filter(order__user=request.user).select_related("product").select_related("order")

    #orders = Order.objects.filter(user=request.user).prefetch_related("orderitem_set")

    return render(request, 'authorization/profile.html', {"form": form, "orders": orders, 'title': 'Bookingcom - Профиль'})


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'authorization/password_reset_form.html'
    #success_url = reverse_lazy('home')
    #success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    #subject_template_name = 'system/email/password_subject_reset_mail.txt'
    #email_template_name = 'system/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'authorization/password_reset_confirm.html'
    #success_url = reverse_lazy('home')
    #success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'
               
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context