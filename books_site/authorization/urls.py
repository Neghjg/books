from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name = 'login'),
    path("logout/", logout_user, name="logout"),
    path("registration/", registration, name="registration"),
]
