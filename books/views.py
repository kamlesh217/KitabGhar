from http.client import HTTPResponse
from django.shortcuts import render
from .models import book_store

# Create your views here.
def home(request):
    return render(request, 'home.html')

def explore(request):

    store=book_store.objects.all()

    return render(request, 'explore.html', {'books':store})

def collection(request):
    store=book_store.objects.all()

    return render(request, 'collection.html', {'books':store} )

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'DashBoard.html')

def account(request):
    return render(request, 'account.html')

