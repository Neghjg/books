# Generated by Django 4.2.7 on 2023-11-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='photos/book-preload.svg', upload_to='photos/', verbose_name='Изображение'),
        ),
    ]
