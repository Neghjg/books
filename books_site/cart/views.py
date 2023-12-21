from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from books.models import Book
from .cart import Cart
from .forms import CartAddProductForm, Promo


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

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
            
            
                return redirect('cart_detail')
            
    else:
        promo = Promo()
        
        
    return render(request, 'cart/detail.html', {'cart': cart, 'promo': promo, "my_promo": my_promo})