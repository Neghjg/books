from django.urls import path
from . import views


app_name = "cart"

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<slug:product_slug>/', views.cart_add, name='cart_add'),
    path('remove/<slug:product_slug>/', views.cart_remove, name='cart_remove'),
    path('change_quantity/<int:item_id>/<int:new_quantity>/', views.cart_change_quantity, name='cart_change'),
]