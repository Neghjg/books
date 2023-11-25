from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id', 'title', 'is_published')
    list_display_links = ("id", "title")
    search_fields = ("title", 'author')
    

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews)

admin.site.site_header = "Админ-панель"