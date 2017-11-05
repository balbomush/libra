from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book

def names(request):
    names = Book.objects.filter(author='Достоевский').order_by('published_date')
    return render(request, 'book/name.html', {'names': names})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})