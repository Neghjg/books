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
from django.contrib import messages


def index(request):
    books = Book.objects.all().order_by('-count_buy')[:10]
    return render(request, 'books/index.html', {'books': books, 'title': 'Bookingcom - Главная'})


def adventures(request):
    sort = request.GET.get('sort', '-count_buy')
    adventures_books = cache.get(sort + "adventures")
    if not adventures_books:
        adventures_books = Book.objects.filter(cat = 5).order_by(sort)
        cache.set(sort + "adventures", adventures_books, 300)
    paginator = Paginator(adventures_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    
    return render(request, 'books/adventures.html', {'books': adventures_books,
                                                     "page_obj": page_obj,
                                                     'sort': sort,
                                                     'cart_product_form': cart_product_form,
                                                     'title': 'Bookingcom - Приключения'})


def detective(request):
    sort = request.GET.get('sort', '-count_buy')
    detective_books = cache.get(sort + "detective")
    if not detective_books:
        detective_books = Book.objects.filter(cat = 4).order_by(sort)
        cache.set(sort + "detective", detective_books, 300)
    paginator = Paginator(detective_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/detective.html', {'books':detective_books,
                                                    "page_obj": page_obj,
                                                    'sort': sort,
                                                    'cart_product_form': cart_product_form,
                                                    'title': 'Bookingcom - Детектив'})


def fantasy(request):
    sort = request.GET.get('sort', '-count_buy')
    fantasy_books = cache.get(sort + 'fantasy')
    if not fantasy_books:
        fantasy_books = Book.objects.filter(cat = 3).order_by(sort)
        cache.set(sort + 'fantasy', fantasy_books, 300)
    paginator = Paginator(fantasy_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/fantasy.html', {'books': fantasy_books,
                                                  "page_obj": page_obj,
                                                  'sort': sort,
                                                  'cart_product_form': cart_product_form,
                                                  'title': 'Bookingcom - Фэнтези'})


def classical_prose(request):
    sort = request.GET.get('sort', '-count_buy')
    classical_prose_books = cache.get(sort + 'classical_prose')
    if not classical_prose_books:
        classical_prose_books = Book.objects.filter(cat = 2).order_by(sort)
        cache.set(sort + 'classical_prose', classical_prose_books, 300)
    paginator = Paginator(classical_prose_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/classical_prose.html', {'books': classical_prose_books,
                                                          "page_obj": page_obj,
                                                          'sort': sort,
                                                          'cart_product_form': cart_product_form,
                                                          'title': 'Bookingcom - Классическая проза'})


def modern_prose(request):
    sort = request.GET.get('sort', '-count_buy')
    modern_prose_books = cache.get(sort + 'modern_prose')
    if not modern_prose_books:
        modern_prose_books = Book.objects.filter(cat = 1).order_by(sort)
        cache.set(sort + 'modern_prose', modern_prose_books, 300)
    paginator = Paginator(modern_prose_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    return render(request, 'books/modern_prose.html', {'books': modern_prose_books,
                                                       "page_obj": page_obj,
                                                       'sort': sort,
                                                       'cart_product_form': cart_product_form,
                                                       'title': 'Bookingcom - Современная проза'})

def search(request):
    result = []
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        result = Book.objects.filter(title__icontains = query) | Book.objects.filter(author__icontains = query) | Book.objects.filter(title__icontains = query.capitalize()) | Book.objects.filter(author__icontains = query.capitalize())
        return render(request, 'books/search.html', {'query': query, 'result': result})
    

def book(request, post_slug):
    book = cache.get(post_slug)
    if not book:
        book = Book.objects.filter(slug = post_slug)
        cache.set(post_slug, book, 1)
    get_book = cache.get('get_book')
    if not get_book:
        get_book = get_object_or_404(Book, slug=post_slug)
        cache.set('get_book', get_book, 300)
    new_comment = None
    #comments = cache.get(post_slug + 'comments')
    #if not comments:
    comments = Reviews.objects.filter(article_id__slug=post_slug).select_related('user')
        #cache.set(post_slug + 'comments', comments, 1)
    avg_rating = cache.get(post_slug + 'rating')
    if not avg_rating:
        avg_rating = Reviews.objects.filter(article_id__slug=post_slug).aggregate(avg = Avg("rating"))
        cache.set(post_slug + 'rating', avg_rating, 300)
    if request.method == 'POST':
        comment_form = Comment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.get_book = get_book
            new_comment.user = request.user
            new_comment.article_id = book[0]
            new_comment.save()
            messages.success(request, f'{request.user.username}, комментарий оставлен')
    else:
        comment_form = Comment()
        
    cart_product_form = CartAddProductForm()

    date_delivary = datetime.now() + timedelta(days=7)
    date_delivary_to_shop = datetime.now() + timedelta(days=3)
    
    return render(request, 'books/book.html', {'book': book,
                                               'get_book': get_book, 
                                               'cart_product_form': cart_product_form,
                                               'new_comment': new_comment,
                                               'comment_form': comment_form,
                                               'comments': comments,
                                               'avg_rating':avg_rating,
                                               'date_delivary':date_delivary,
                                               "date_delivary_to_shop":date_delivary_to_shop,
                                               "title": book[0]})

def author(request, book_author):
    author = Book.objects.filter(author_slug_URL=book_author)
    author_name = author[0].author
    return render(request, 'books/author.html', {'author': author, 'author_name': author_name, 'title':author_name})
#<!--{% url 'author' i.author %}-->

