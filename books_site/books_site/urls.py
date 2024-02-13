"""
URL configuration for books_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from books_site import settings
from books.views import *
from django.contrib.sitemaps.views import sitemap
from books.sitemaps import BookSitemap, CatsSitemap, HomeSitemap
from django.views.decorators.cache import cache_page


sitemaps = {
    'books': BookSitemap,
    'cats': CatsSitemap,
    'main_page': HomeSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace="orders")),
    path("", include('books.urls', namespace="main")),
    path('authorization/', include('authorization.urls', namespace="authorization")),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('sitemap.xml', cache_page(60 * 15)(sitemap), {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:
    
    urlpatterns =[
       path("__debug__/", include("debug_toolbar.urls")), 
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

