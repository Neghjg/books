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
    path('order_add/<int:pk>/', views.OrderAddView.as_view(), name = 'order_add'),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
