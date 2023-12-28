from django.conf import settings
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from orders.models import Order
from django.contrib.auth.models import User
from huey import RedisHuey, crontab
#import huey
from huey.contrib.djhuey import db_task
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import send_mail
from huey.contrib import djhuey as huey



#huey_instance = huey.Huey()
#huey = RedisHuey("orders")


#@huey_instance.task()
#@huey.task()

@huey.db_task()
def order_created(order_id, user_em):
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа: {}'.format(order_id)
    message = '{},\n\nВаш заказ оформлен.\
                Номер вашего заказа: {}.'.format(order.first_name,
                                             order.id)
    #try:
    mail_sent = send_mail(subject,
                          message,
                          'jovannymoriarty@yandex.ru',
                          [user_em])
    #except smtplib.SMTPException:
    #    print("Ошибка: Невозможно отправить сообщение")
    return mail_sent


@huey.db_task()
def order_created_non_auth(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа: {}'.format(order_id)
    message = '{},\n\nВаш заказ оформлен.\
                Номер вашего заказа: {}.'.format(order.first_name,
                                             order.id)
    
    
    mail_sent = send_mail(subject,
                          message,
                          'jovannymoriarty@yandex.ru',
                          [order.email])
    return mail_sent