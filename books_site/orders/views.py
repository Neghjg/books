from django.shortcuts import render, redirect
from .models import OrderItem, Book, Order
from cart.cart import Cart
from .tasks import order_created, order_created_non_auth
from django.contrib.auth.decorators import login_required
from .forms import NonAuthenticatedUserForm, AuthenticatedUserForm
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.urls import reverse
from payment.views import payment_process
from orders.utils import requires_delivery, payment_on_get


@login_required
def order_create_authenticated_users(request):
    us = request.user
    cart = Cart(request)
    my_promo = request.session.get('promokod', '0')
    if request.method == 'POST':
        form = AuthenticatedUserForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    
                    order = form.save()
                    if request.session.get('promokod', '0') == "1":
                        for item in cart:
                            OrderItem.objects.create(order=order,
                                                 product=item['product'],
                                                 price=((item['price'])/10)*9,
                                                 quantity=item['quantity']
                                                 )
                            book = Book.objects.get(title = item['product'])
                            if book.quantity < item['quantity']:
                                raise ValidationError(f'Недостаточное количество товара на складе\
                                                       В наличии - {book.quantity}')
                            book.quantity -= item['quantity']
                            book.count_buy += item['quantity'] 
                            book.save()
                        request.session["promokod"] = "2"
                    else:
                        for item in cart:
                            OrderItem.objects.create(order=order,
                                                 product=item['product'],
                                                 price=item['price'],
                                                 quantity=item['quantity'],
                                                 )
                            book = Book.objects.get(title = item['product'])
                            if book.quantity < item['quantity']:
                                raise ValidationError(f'Недостаточное количество товара на складе\
                                                       В наличии - {book.quantity}')
                            book.quantity -= item['quantity']
                            book.count_buy += item['quantity'] 
                            book.save()
                    # очистка корзины
                    send_email = form.cleaned_data.get('email')
                    Order.objects.filter(id = order.id).update(email = send_email, user = us, first_name = us.first_name, last_name = us.last_name )
                    cart.clear()
                    order_created(order.id, send_email)
                    request.session['order_id'] = order.id
                    pay = form.cleaned_data.get('payment_on_get')
                    if pay == '0':
                        return payment_process(request)
                    else:
                        messages.success(request, f'Заказ №{order.id} оформлен! ' 
                            f'Способ доставки: {requires_delivery(form.cleaned_data.get("requires_delivery"),form.cleaned_data.get("address"))} \n'
                            f'Оплата: {payment_on_get(form.cleaned_data.get("payment_on_get"))}')
                        return redirect('main:home')
                        #return render(request, 'orders/created.html',
                        #  {'order': order, "my_promo": my_promo})
                    
                    
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('main:home')
    else:
        form = AuthenticatedUserForm(instance=request.user)
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, "my_promo": my_promo, 'title': 'Bookingcom - Заказ'})
    
def order_create_non_authenticated_users(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = NonAuthenticatedUserForm(request.POST)
        if form.is_valid():
            order = form.save()
            if request.session.get('promokod', '0') == "1":
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=((item['price'])/10)*9,
                                             quantity=item['quantity'])
                    book = Book.objects.get(title = item['product'])
                    if book.quantity < item['quantity']:
                        raise ValidationError(f'Недостаточное количество товара на складе\
                                                В наличии - {book.quantity}')
                    book.quantity -= item['quantity']
                    book.count_buy += item['quantity'] 
                    book.save()
                request.session["promokod"] = "2"
            else:
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                    book = Book.objects.get(title = item['product'])
                    if book.quantity < item['quantity']:
                        raise ValidationError(f'Недостаточное количество товара на складе\
                                                       В наличии - {book.quantity}')
                    book.quantity -= item['quantity']
                    book.count_buy += item['quantity'] 
                    book.save()
            # очистка корзины
            cart.clear()
            order_created_non_auth(order.id)
            request.session['order_id'] = order.id
            pay = form.cleaned_data.get('payment_on_get')
            if pay == '0':
                return payment_process(request)
            else:
                messages.success(request, f'Заказ №{order.id} оформлен! ' 
                    f'Способ доставки: {requires_delivery(form.cleaned_data.get("requires_delivery"),form.cleaned_data.get("address"))} \n'
                    f'Оплата: {payment_on_get(form.cleaned_data.get("payment_on_get"))}')
                return redirect('main:home')
                #return render(request, 'orders/created.html',
                #          {'order': order})
    else:
        form = NonAuthenticatedUserForm()
    return render(request, 'orders/create_non-authenticated.html',
                  {'cart': cart, 'form': form, 'title': 'Bookingcom - Заказ'})
