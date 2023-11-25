from django.shortcuts import render
from .models import *


# Create your views here.
def idex(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})