from django.urls import path
from . import views


app_name = "books"

urlpatterns = [
    path('book_api/', views.BookListView.as_view(), name = "book_api"),
    path('book_api/<int:pk>/', views.BookDetailView.as_view(), name = "book_api_detail"),
    path('cat_api/', views.CatList.as_view(), name = "cat_api"),
    path('cat_api/<int:pk>/', views.CatDetail.as_view(), name = "cat_api_detail"),
    #path('orderitem_api/', views.OrderItemListView.as_view(), name = "orderitem_api"),
    #path('orderitem_api/<pk>/', views.OrderItemDetail.as_view(), name = "orderitem_api_detail"),
    path('order_api/', views.OrderListView.as_view(), name = "order_api"),
    path('order_api/<int:pk>/', views.OrderDetail.as_view(), name = "order_api_detail"),
    path('order_api/<int:pk>/<int:quantity>/add_order', views.OrderAddView.as_view(), name = 'order_add')
]
