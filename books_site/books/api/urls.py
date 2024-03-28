from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from books.api.views import BookViewSet, CatViewSet, OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
