from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from books.models import Book
from .cart import Cart
from .forms import CartAddProductForm, Promo
from django.contrib import messages
from django.forms import ValidationError
from django.http import JsonResponse
from django.template.loader import render_to_string



@require_POST
def cart_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Book, slug=product_slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        try:
            cd = form.cleaned_data
            quantity = cd['quantity']
            if product.quantity < quantity:
                raise ValidationError(f"Недостаточное количество товара на складе\
                                        В наличии - {product.quantity}")
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
            messages.success(request, f'"{product}" успешно добавлена в корзину')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect(request.META['HTTP_REFERER'])
            
    return redirect(request.META['HTTP_REFERER'])

def cart_remove(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Book, slug=product_slug)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    my_promo = request.session.get('promokod', '0')
    if request.method == 'POST':
        promo = Promo(request.POST)
        if promo.is_valid():
            cd = promo.cleaned_data
            if cd["promo"] == "prom":
                if request.session.get('promokod', '0') == "0":
                    request.session['promokod'] = "1"
                    my_promo = request.session.get('promokod', '0')
                    print(my_promo)
                elif request.session.get('promokod', '0') != "0":
                    request.session['promokod'] = "2"
                    my_promo = request.session.get('promokod', '0')
                return redirect('cart:cart_detail')
    else:
        promo = Promo()
    return render(request, 'cart/detail.html', {'cart': cart,
                                                'promo': promo,
                                                "my_promo": my_promo,
                                                'title': 'Bookingcom - Корзина'})
    

def cart_change_quantity(request, item_id, new_quantity):
    cart = Cart(request)
    cart.change_quantity(item_id, new_quantity)
    return JsonResponse({'success': True})