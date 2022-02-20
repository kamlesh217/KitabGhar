from django.shortcuts import render
from django.http import HttpResponse
from .models import book_store
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login, authenticate
# Create your views here.




def explore(request):
    book=book_store.objects.all()
    return render(request, 'books/explore.html', {'books':book})



def dashboard(request):
    if request.user.is_authenticated:
       return render(request, 'books/DashBoard.html' )
    else:
        return redirect('/')


def register(request):
    
    if request.method=="POST":
        fname=request.POST['fname']
        email=request.POST['email']
        username=request.POST['email']
        password=request.POST['password']
        lname=request.POST['lname']

        if User.objects.filter(email=email).exists():
            return redirect('register')
        else:  
            user=User.objects.create_user(username=username, email=email, first_name=fname,password=password, last_name=lname )
           
            user.save()
            return redirect('/')
    else:
        return render(request, 'books/register.html')


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        else:
            return render(request, 'books/home.html')


def account(request):
    if request.user.is_authenticated:
        return render(request, 'books/Account.html' )
        
    else:
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')



def comment(request):
    if request.method=='POST':
        user="dsa"
   
    return redirect('/collection')

