from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import requests
from django.db.models import Q
from django.db.models import Avg
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from datetime import datetime 
from datetime import timedelta 
from django.core.cache import cache

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('-count_buy')[:10]
    return render(request, 'books/index.html', {'books': books})


def adventures(request):
    adventures_sort = request.GET.get('adventures_sort', '-count_buy')
    print(adventures_sort)
    adventures_books = cache.get(adventures_sort + "adventures")
    if not adventures_books:
        adventures_books = Book.objects.filter(cat = 5).order_by(adventures_sort)
        cache.set(adventures_sort + "adventures", adventures_books, 3)
    paginator = Paginator(adventures_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    
    return render(request, 'books/adventures.html', {'books': adventures_books, "page_obj": page_obj, 'adventures_sort': adventures_sort,
                                                     'cart_product_form': cart_product_form})


def detective(request):
    detective_sort = request.GET.get('detective_sort', '-count_buy')
    print(detective_sort)
    detective_books = cache.get(detective_sort + "detective")
    if not detective_books:
        detective_books = Book.objects.filter(cat = 4).order_by(detective_sort)
        cache.set(detective_sort + "detective", detective_books, 3)
    paginator = Paginator(detective_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/detective.html', {'books':detective_books, "page_obj": page_obj, 'detective_sort': detective_sort,
                                                     'cart_product_form': cart_product_form})


def fantasy(request):
    sort = request.GET.get('sort', '-count_buy')
    books = Book.objects.filter(cat = 3).order_by(sort)
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/fantasy.html', {'books': books, "page_obj": page_obj, 'sort': sort,
                                                     'cart_product_form': cart_product_form})


def classical_prose(request):
    sort = request.GET.get('sort', '-count_buy')
    books = Book.objects.filter(cat = 2).order_by(sort)
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/classical_prose.html', {'books': books, "page_obj": page_obj, 'sort': sort,
                                                     'cart_product_form': cart_product_form})


def modern_prose(request):
    sort = request.GET.get('sort', '-count_buy')
    books = Book.objects.filter(cat = 1).order_by(sort)
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/modern_prose.html', {'books': books, "page_obj": page_obj, 'sort': sort,
                                                     'cart_product_form': cart_product_form})

def search(request):
    result = []
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        result = Book.objects.filter(title__icontains = query) | Book.objects.filter(author__icontains = query) | Book.objects.filter(title__icontains = query.capitalize()) | Book.objects.filter(author__icontains = query.capitalize())
        return render(request, 'books/search.html', {'query': query, 'result': result})
    

def book(request, post_slug):
    book = Book.objects.filter(slug = post_slug)
    #get_book = cache.get('get_book')
    #if not get_book:
    get_book = get_object_or_404(Book, slug=post_slug)
        #cache.set('get_book', get_book, 100)
    new_comment = None
    comments = Reviews.objects.filter(article_id__slug=post_slug).select_related('user')
    avg_rating = Reviews.objects.filter(article_id__slug=post_slug).aggregate(avg = Avg("rating"))
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
        
    cart_product_form = CartAddProductForm()
    
    date_delivary = datetime.now() + timedelta(days=7)
    date_delivary_to_shop = datetime.now() + timedelta(days=3)
    
    
    return render(request, 'books/book.html', {'book': book, 'get_book': get_book, 
                                               'cart_product_form': cart_product_form,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form,
                                               'comments': comments,
                                               'avg_rating':avg_rating,
                                               'date_delivary':date_delivary,
                                               "date_delivary_to_shop":date_delivary_to_shop})

def author(request, book_author):
    books = Book.objects.filter(author=book_author)
    return render(request, 'books/author.html', {'books': books})
#<!--{% url 'author' i.author %}-->

