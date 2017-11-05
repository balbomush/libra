from django.shortcuts import render

# Create your views here.
def names(request):
    return render(request, 'book/name.html', {})