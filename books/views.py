from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def store(request):
    return render(request, 'store.html')

def explore(request):
    return render(request, 'explore.html')

def collection(request):
    return render(request, 'collection.html')

def register(request):
    return render(request, 'register.html')
