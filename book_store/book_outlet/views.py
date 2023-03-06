from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg

from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    context = {
        "books": books,
        "total_no_of_books": num_books,
        "avg_rating": avg_rating
    }
    return render(request, "book_outlet/index.html", context)

def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    context = {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling 
    }
    return render(request, "book_outlet/book_detail.html", context)