from django.urls import path
from . import views
from . import utils


app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('webhook/', utils.stripe_webhook, name='stripe-webhook'),
]
