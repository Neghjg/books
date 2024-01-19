from django.shortcuts import render
from .models import OrderItem, Book, Order
#from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from .tasks import order_created_non_auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NonAuthenticatedUserForm, AuthenticatedUserForm



# def order_create(request):
#     cart = Cart(request)
    
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order,
#                                          product=item['product'],
#                                          price=item['price'],
#                                          quantity=item['quantity'])
#             # очистка корзины
#             cart.clear()
#             order_created(order.id)
#             return render(request, 'orders/created.html',
#                           {'order': order})
#     else:
#         form = OrderCreateForm
#     return render(request, 'orders/create.html',
#                   {'cart': cart, 'form': form})


@login_required
def order_create_authenticated_users(request):
    us = request.user
    user_em = us.email
    cart = Cart(request)
    my_promo = request.session.get('promokod', '0')
    if request.method == 'POST':
        form = AuthenticatedUserForm(request.POST)
        if form.is_valid():
            
            order = form.save()
            
            
            if request.session.get('promokod', '0') == "1":
                
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=((item['price'])/10)*9,
                                             quantity=item['quantity'])
                    
                request.session["promokod"] = "2"
            else:
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'],
                                             )
                    
                    
                #print(item['product'])
                #item_id[]
                    book = Book.objects.get(title = item['product'])
                    book.count_buy += item['quantity'] 
                    book.save()
            # очистка корзины
            Order.objects.filter(id = order.id).update(email = user_em)
            cart.clear()
            order_created(order.id, user_em)
            return render(request, 'orders/created.html',
                          {'order': order, "my_promo": my_promo})
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
                request.session["promokod"] = "2"
            else:
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            order_created_non_auth(order.id)
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = NonAuthenticatedUserForm()
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})
