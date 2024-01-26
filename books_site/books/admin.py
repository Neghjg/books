from django.contrib import admin
from .models import *

# Register your models here.
class ReviewsTabAdmin(admin.TabularInline):
    model = Reviews
    fields = ('id', 'user', 'rating', 'comment')
    search_fields = ('user', 'rating',)
    readonly_fields = ('id', 'user',)
    extra = 1


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title'], 'author_slug_URL': ['author']}
    list_display = ('id', 'title', 'author', 'cat', 'is_published', 'quantity')
    list_display_links = ("id", "title")
    search_fields = ("title", 'author')
    list_editable=('is_published',)
    list_filter=("cat", 'is_published', 'author')
    fields = (
          'title',
          'slug',
          'description',
          'cat',
          'photo',
          'quantity',
          'price',
          'is_published',
          'count_buy',
          'author',
          'author_slug_URL',
          'year_of_publication',
          'publisher',
          'ISBN',
          'number_of_pages',
          ('size', 'type_of_cover'),
          'weight',
          'age_restrictions',
    )
    inlines = [ReviewsTabAdmin,]
    

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
    readonly_fields = ('user',)
    

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)

admin.site.site_header = "Админ-панель"