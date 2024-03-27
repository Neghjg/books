from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from books.api.views import BookViewSet, CatViewSet, OrderViewSet


router = routers.SimpleRouter()
router.register('book', BookViewSet)
router.register('cat', CatViewSet)
router.register('order', OrderViewSet)

app_name = "books"

urlpatterns = [
    path('', include(router.urls)),
    #path('b', views.BookAPIView.as_view()),
    #path('book_api/', views.BookListView.as_view(), name = "book_api"),
    #path('book_api/<int:pk>/', views.BookDetailView.as_view(), name = "book_api_detail"),
    #path('cat_api/', views.CatList.as_view(), name = "cat_api"),
    #path('cat_api/<int:pk>/', views.CatDetail.as_view(), name = "cat_api_detail"),
    #path('orderitem_api/', views.OrderItemListView.as_view(), name = "orderitem_api"),
    #path('orderitem_api/<pk>/', views.OrderItemDetail.as_view(), name = "orderitem_api_detail"),
    #path('order_api/', views.OrderListView.as_view(), name = "order_api"),
    #path('order_api/<int:pk>/', views.OrderDetail.as_view(), name = "order_api_detail"),
    path('order_add/<int:pk>/', views.OrderAddView.as_view(), name = 'order_add'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
