from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id', 'title', 'cat', 'is_published')
    list_display_links = ("id", "title")
    search_fields = ("title", 'author')
    

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")
    
class ReviewsAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug':('id',)}
    list_display = ('id', 'user', 'rating', 'comment')
    list_display_links = ("id", "user")
    search_fields = ("user", 'id')
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)

admin.site.site_header = "Админ-панель"