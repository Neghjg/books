# Generated by Django 4.2.7 on 2024-01-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_alter_book_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
    ]
