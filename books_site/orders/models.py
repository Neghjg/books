from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from django.conf import settings


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="email")
    address = models.CharField(max_length=250, verbose_name="Адрес", blank=True)
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    postal_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    paid = models.BooleanField(default=False, verbose_name="Статус оплаты")
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус заказа')
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name="user", default=None)
    payment_id = models.CharField(max_length=250, blank=True)
    

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
    def get_payment_url(self):
        if not self.payment_id:
            # никаких ассоциированных платежей
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:
            # путь Stripe для тестовых платежей
            path = '/test/'
        else:
            # путь Stripe для настоящих платежей
            path = '/'
        return f'https://dashboard.stripe.com{path}payments/{self.payment_id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Book, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name = 'Проданные товары'
        verbose_name_plural = 'Проданные товары'
        

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
