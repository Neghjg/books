from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<slug:product_slug>/', views.cart_add, name='cart_add'),
    #path('change/<product_id>/', views.cart_change, name='cart_change'),
    path('remove/<slug:product_slug>/', views.cart_remove, name='cart_remove'),
]