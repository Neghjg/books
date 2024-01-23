from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='photos/', default='photos/book-preload.svg', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    count_buy = models.IntegerField(verbose_name='Количесвто покупок')
    author = models.CharField(max_length=255, verbose_name='автор')
    year_of_publication = models.IntegerField(verbose_name='Год издания')
    publisher = models.CharField(max_length=100, verbose_name='Издательсво')
    ISBN = models.CharField(max_length=255, verbose_name='ISBN', default="978-5-38-924083-4")
    number_of_pages = models.IntegerField(verbose_name='Количесвто страниц', default=1760)
    size = models.CharField(max_length=255, verbose_name='Размер' , default="21.5x14.5x8.8")
    type_of_cover = models.CharField(max_length=255, verbose_name='Тип обложки', default="Твердый переплёт")
    weight = models.IntegerField(verbose_name='Вес', default=2010)
    age_restrictions = models.IntegerField(verbose_name='Возрастные ограничения', default=8)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book', kwargs={'post_slug': self.slug})
    
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
    article_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True, related_name='comments_book')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    rating = models.IntegerField(verbose_name='Оценка')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
    
    def __str__(self):
        return str(self.user)
    
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'