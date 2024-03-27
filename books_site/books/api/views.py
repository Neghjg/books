from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Book, Category
from books.api.serializers import BookSerializer, CatSerializer, OrderItemSerializer, OrderSerializer
from orders.models import OrderItem, Order
from django.forms import ValidationError
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action


#class BookListView(generics.ListAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
    
    
#class BookDetailView(generics.RetrieveAPIView):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer
    
    
#class BookAPIView(APIView):
#    def get(self, request):
#        queryset = Book.objects.all().order_by("id")
#        return Response(BookSerializer(queryset, many=True).data)    

    
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    
#class CatList(generics.ListAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CatSerializer
    
    
#class CatDetail(generics.RetrieveAPIView):
#    queryset = Category.objects.all()
#    serializer_class = CatSerializer

class CatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().distinct()
    serializer_class = CatSerializer

#class OrderListView(generics.ListAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer
    
    
#class OrderDetail(generics.RetrieveAPIView):
#    queryset = Order.objects.all()
#    serializer_class = OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related("user").prefetch_related("items", "items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    
    
#class OrderAddView(APIView):
class OrderAddView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(methods=['post'], detail=True)
    def post(self, request, pk, quantity, format=None):
        try:
            book = Book.objects.get(id=pk)
        except:
            return Response({'error': 'Книги не существует'})
        if request.data['requires_delivery'] == 'True':
            order = Order.objects.create(
                user = request.user,
                email = request.user.email,
                first_name = request.user.first_name,
                last_name = request.user.last_name,
                address = request.data['address'],
                requires_delivery = True,
                payment_on_get = True
            )
        else:
            order = Order.objects.create(
                user = request.user,
                email = request.user.email,
                first_name = request.user.first_name,
                last_name = request.user.last_name,
                requires_delivery = False,
                payment_on_get = True
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
        
        