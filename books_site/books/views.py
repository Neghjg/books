from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from orders.models import Order
from django.db.models import Avg
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from datetime import datetime 
from datetime import timedelta 
from django.core.cache import cache
from django.contrib import messages
from books.utils import q_search
from django.db.models import Count
from taggit.models import Tag


def index(request):
    books = Book.objects.all().order_by('-count_buy')[:10]
    
    if request.user.is_authenticated:
        orders_user = Order.objects.filter(user=request.user).order_by('-created')[:10].prefetch_related("items").values_list("items__product", flat=True)
        books_order = Book.objects.filter(id__in=orders_user).prefetch_related("tags")
        books_tags_ids = books_order.values_list('tags__id', flat=True)
        simular_books = Book.objects.filter(tags__in=books_tags_ids).exclude(id__in=orders_user)
        simular_books = simular_books.annotate(same_tags=Count('tags')).order_by('-same_tags','-count_buy')[:6]
    else:
        simular_books = None
    
    return render(request, 'books/index.html', {'books': books,
                                                'simular_books': simular_books,
                                                'title': 'Bookingcom - Главная'})


def category(request, category_slug=None):
    sort = request.GET.get('sort', '-count_buy')
    category_books = cache.get(sort + category_slug)
    if not category_books:
        category_books = Book.objects.filter(cat__slug = category_slug).order_by(sort)
        cache.set(sort + category_slug, category_books, 300)
    title_category = Category.objects.get(slug=category_slug)
    paginator = Paginator(category_books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    
    return render(request, 'books/category.html', {'books': category_books,
                                                   'slug_url': category_slug,
                                                   "page_obj": page_obj,
                                                   'sort': sort,
                                                   "cart_product_form": cart_product_form,
                                                   "title": 'Bookingcom - Категории',
                                                   "title_category": title_category})

    
def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        result = q_search(query)
    return render(request, 'books/search.html', {"page_obj": result})


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

