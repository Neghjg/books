from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def adventures(request):
    books = Book.objects.filter(cat = 5)
    return render(request, 'books/adventures.html', {'books': books})

def detective(request):
    books = Book.objects.filter(cat = 4)
    return render(request, 'books/detective.html', {'books': books})

def fantasy(request):
    books = Book.objects.filter(cat = 3)
    return render(request, 'books/fantasy.html', {'books': books})

def classical_prose(request):
    books = Book.objects.filter(cat = 2)
    return render(request, 'books/classical_prose.html', {'books': books})

def modern_prose(request):
    books = Book.objects.filter(cat = 1)
    return render(request, 'books/modern_prose.html', {'books': books})