from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='media/photos/', default='photos/book-preload.svg', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    is_published = models.BooleanField(default=True)
    count_buy = models.IntegerField(verbose_name='Количесвто покупок')
    author = models.CharField(max_length=255, verbose_name='автор')
    year_of_publication = models.IntegerField(verbose_name='Год издания')
    publisher = models.CharField(max_length=100, verbose_name='Издательсво')
    rev = models.ForeignKey('Reviews', on_delete=models.PROTECT, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        #ordering = ['time_create', 'title']
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Наименование группы")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ManyToManyField(User)
    rating = models.IntegerField(verbose_name='Оценка')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'