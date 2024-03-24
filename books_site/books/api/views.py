from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Book, Category
from books.api.serializers import BookSerializer, CatSerializer, OrderItemSerializer, OrderSerializer
from orders.models import OrderItem, Order
from django.forms import ValidationError


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class CatList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    
class CatDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    
    
#class OrderItemListView(generics.ListAPIView):
#    queryset = OrderItem.objects.all()
#    serializer_class = OrderItemSerializer
    
#class OrderItemDetail(generics.RetrieveAPIView):
#    queryset = OrderItem.objects.all()
#    serializer_class = OrderItemSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderAddView(APIView):
    def post(self, request, pk, quantity, format=None):
        book = Book.objects.get(id=pk)
        order = Order.objects.create(
            user = request.user,
            email = request.user.email,
            first_name = request.user.first_name,
            last_name = request.user.last_name
        )
        OrderItem.objects.create(order=order,
                                product=book,
                                price=book.price,
                                quantity=quantity,
                                )
        if book.quantity < quantity:
            raise ValidationError(f'Недостаточное количество товара на складе\
                                    В наличии - {book.quantity}')
        book.quantity -= quantity
        book.count_buy += quantity
        return Response({'succes': True})
        
        