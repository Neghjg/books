from django.shortcuts import render
from .models import *
import requests


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def adventures(request):
    sort = request.GET.get('sort', 'default')
    if sort == 'default':
        books = Book.objects.filter(cat = 5)
    elif sort == 'price_to_low':
        books = Book.objects.filter(cat = 5).order_by('price')
    elif sort == 'price_to_hight':
        books = Book.objects.filter(cat = 5).order_by('-price')
    return render(request, 'books/adventures.html', {'books': books})

def detective(request):
    sort = request.GET.get('sort', 'default')
    if sort == 'default':  
        books = Book.objects.filter(cat = 4)
    elif sort == 'price_to_low':
        books = Book.objects.filter(cat = 4).order_by('price')
    elif sort == 'price_to_hight':
        books = Book.objects.filter(cat = 4).order_by('-price')
    return render(request, 'books/detective.html', {'books': books})

def fantasy(request):
    sort = request.GET.get('sort', 'default')
    if sort == 'default':  
        books = Book.objects.filter(cat = 3)
    elif sort == 'price_to_low':
        books = Book.objects.filter(cat = 3).order_by('price')
    elif sort == 'price_to_hight':
        books = Book.objects.filter(cat = 3).order_by('-price')
    return render(request, 'books/fantasy.html', {'books': books})

def classical_prose(request):
    sort = request.GET.get('sort', 'default')
    if sort == 'default':  
        books = Book.objects.filter(cat = 2)
    elif sort == 'price_to_low':
        books = Book.objects.filter(cat = 2).order_by('price')
    elif sort == 'price_to_hight':
        books = Book.objects.filter(cat = 2).order_by('-price')
    return render(request, 'books/classical_prose.html', {'books': books})

def modern_prose(request):
    sort = request.GET.get('sort', 'default')
    if sort == 'default':  
        books = Book.objects.filter(cat = 1)
    elif sort == 'price_to_low':
        books = Book.objects.filter(cat = 1).order_by('price')
    elif sort == 'price_to_hight':
        books = Book.objects.filter(cat = 1).order_by('-price')
    return render(request, 'books/modern_prose.html', {'books': books})