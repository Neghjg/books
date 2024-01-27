from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login, name = 'login'),
    path("logout/", logout_user, name="logout"),
    path("registration/", registration, name="registration"),
    path('profile/', profile, name='profile'),
    #path('', include('django.contrib.auth.urls')),
    path('reset_password/', UserForgotPasswordView.as_view(template_name='authorization/password_reset_form.html'),
         name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='authorization/password_reset_done.html'),
         name ='password_reset_done'),
    path('reset/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(template_name='authorization/password_reset_confirm.html'),
          name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authorization/password_reset_complete.html'),
         name ='password_reset_complete'),
]
