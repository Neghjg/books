# Generated by Django 4.2.7 on 2024-02-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitem_options_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
