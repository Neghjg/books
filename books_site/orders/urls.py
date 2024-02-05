from django.urls import path, include
from . import views


app_name = "orders"

urlpatterns = [
    #path('create/', views.order_create, name='order_create'),
    path('create/', views.order_create_authenticated_users, name='order_create'),
    path('create_non-authenticated/', views.order_create_non_authenticated_users, name='order_create_non_authenticated'),
]