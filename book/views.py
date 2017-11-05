from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book
from .forms import PostForm

def names(request):
    names = Book.objects.filter(author='Достоевский').order_by('published_date')
    return render(request, 'book/name.html', {'names': names})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def book_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = PostForm()
    return render(request, 'book/book_edit.html', {'form': form})