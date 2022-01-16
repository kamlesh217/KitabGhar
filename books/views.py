import email
from http.client import HTTPResponse
from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from .models import book_store
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/')

    else:
        return render(request, 'home.html')

def explore(request):
    if request.user.is_authenticated:
        store=book_store.objects.all()
        return render(request, 'explore.html', {'books':store})
    else:
        return redirect('/')

    

def collection(request):
    if request.user.is_authenticated:
        store=book_store.objects.all()
        return render(request, 'collection.html', {'books':store} )
    else:
        return redirect('/')

def register(request):
    
    if request.method=="POST":
        fname=request.POST['name']
        email=request.POST['email']
        username=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(email=email).exists():
            return redirect('register')
        else:  
            user=User.objects.create_user(username=username, email=email, first_name=fname,password=password)
            user.save()
            return redirect('/')
    else:
        return render(request, 'register.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'DashBoard.html' )
    else:
        return redirect('/')
    

def account(request):
    if request.user.is_authenticated:
        return render(request, 'Account.html' )
    else:
        return redirect('/')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
