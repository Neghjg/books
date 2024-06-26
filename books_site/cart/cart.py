from decimal import Decimal
from django.conf import settings
from books.models import Book


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in
               self.cart.values())
        
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
    def change_quantity(self, item_id, new_quantity):
        item_id = str(item_id)
        if item_id in self.cart:
            self.cart[item_id]['quantity'] = new_quantity
            self.save()
            
    def __getitem__(self, key):
        return self.cart[key]

    def __setitem__(self, key, value):
        self.cart[key] = value
        self.save()