from rest_framework import serializers
from books.models import Book, Category
from orders.models import OrderItem, Order
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', 'slug', 'price']
        
        
class CatSerializer(serializers.ModelSerializer):
    book = BookSerializer(many = True, read_only=True, source='book_set')
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'book']
        


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email']
        
        
class OrderItemSerializer(serializers.ModelSerializer):
    product = BookSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']
        
        
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    orderitem = OrderItemSerializer(source='items', many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'paid', 'address', 'requires_delivery', 'payment_on_get', 'status', 'user', 'orderitem']
        