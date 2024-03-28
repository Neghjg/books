from rest_framework import generics
from rest_framework.response import Response
from books.models import Book, Category
from books.api.serializers import BookSerializer, CatSerializer, OrderSerializer
from orders.models import OrderItem, Order
from django.forms import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
   
  
class PaginationBookAndOrder(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50
  
  
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    pagination_class = PaginationBookAndOrder
    

class CatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().distinct()
    serializer_class = CatSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related("user").prefetch_related("items", "items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PaginationBookAndOrder
    
    

class OrderAddView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    #authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(methods=['post'], detail=True)
    def post(self, request, pk, format=None):
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
                                quantity=request.data['quantity'],
                                )
        if book.quantity < request.data['quantity']:
            raise ValidationError(f'Недостаточное количество товара на складе\
                                    В наличии - {book.quantity}')
        book.quantity -= request.data['quantity']
        book.count_buy += request.data['quantity']
        
        return Response({'succes': True})
        
        