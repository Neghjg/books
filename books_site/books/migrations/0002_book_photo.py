# Generated by Django 4.2.7 on 2023-11-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(default='photos/book-preload.svg', upload_to='photos/', verbose_name='Изображение'),
        ),
    ]
