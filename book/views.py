from django.shortcuts import render
from django.utils import timezone
from .models import Book

def names(request):
    names = Book.objects.filter(author='Достоевский').order_by('published_date')
    return render(request, 'book/name.html', {'names': names})