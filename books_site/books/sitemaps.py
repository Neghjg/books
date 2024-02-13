from django.contrib.sitemaps import Sitemap
from .models import Book, Category
from django.urls import reverse


class BookSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Book.objects.all()
    
    
    
class CatsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    
    def items(self):
        return Category.objects.all()
    
    

class HomeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5
    
    def items(self):
        return ["main:home"]
    
    def location(self, item):
        return reverse(item)
    
    #def lastmod(self, obj):
    #    return obj.updated
    
