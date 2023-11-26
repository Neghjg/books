from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def adventures(request):
    
    books = Book.objects.filter(cat = 5)
    return render(request, 'books/adventures.html', {'books': books})