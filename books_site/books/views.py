from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
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

def search(request):
    result = []
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        result = Book.objects.filter(title__istartswith = query)
        return render(request, 'books/search.html', {'query': query, 'result': result})
    
    
def book(request, post_slug):
    book = Book.objects.filter(slug = post_slug)
    get_book = get_object_or_404(Book, slug=post_slug)
    new_comment = None
    
    if request.method == 'POST':
        comment_form = Comment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.get_book = get_book
            new_comment.user = request.user
            new_comment.article_id = book[0]
            new_comment.save()
    else:
        comment_form = Comment()
    return render(request, 'books/book.html', {'book': book, 'get_book': get_book, 
                                               
                                               'new_comment': new_comment,
                                               'comment_form': comment_form})

def author(request, book_author):
    books = Book.objects.filter(author=book_author)
    return render(request, 'books/author.html', {'books': books})
#<!--{% url 'author' i.author %}-->


            