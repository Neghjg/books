from django.shortcuts import render, redirect
from .models import OrderItem, Book, Order
from cart.cart import Cart
from .tasks import order_created, order_created_non_auth
from django.contrib.auth.decorators import login_required
from .forms import NonAuthenticatedUserForm, AuthenticatedUserForm
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError


@login_required
def order_create_authenticated_users(request):
    us = request.user
    user_em = us.email
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
                    Order.objects.filter(id = order.id).update(email = user_em, user = us, first_name = us.first_name, last_name = us.last_name )
                    cart.clear()
                    order_created(order.id, user_em)
                    messages.success(request, 'Заказ оформлен!')
                    return render(request, 'orders/created.html',
                          {'order': order, "my_promo": my_promo})
                    
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('home')
    else:
        form = AuthenticatedUserForm()
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, "my_promo": my_promo})
    
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
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = NonAuthenticatedUserForm()
    return render(request, 'orders/create_non-authenticated.html',
                  {'cart': cart, 'form': form})
