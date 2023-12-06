# Generated by Django 4.2.7 on 2023-12-02 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_book_rev_reviews_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='article_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book'),
        ),
    ]
