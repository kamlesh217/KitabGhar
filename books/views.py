
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import book_collection, book_store
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login, authenticate


# Create your views here.
def home(request):
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
            return render(request, 'home.html')

def explore(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.user.username
            book_name=request.POST.get('book')
            store=book_store.objects.all()
            return render(request, 'explore.html', {'books':store})
        else:
            store=book_store.objects.all()
            return render(request, 'explore.html', {'books':store})
    else:
        return redirect('/')
        

    

def collection(request):
    if request.user.is_authenticated:
        collect=book_collection.objects.all()
        return render(request, 'collection.html', {'books':collect} )
        
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
    

def logoutuser(request):
    logout(request)
    return redirect('/')

def remove(request):
    if request.method=='POST':
        user="dsa"
   
    return redirect('/collection')

def comment(request):
    if request.method=='POST':
        user="dsa"
   
    return redirect('/collection')

def add(request):
    if request.method=='POST':
        user="dsa"

    
    return redirect('/explore')

def pdf(request):
    print(45)
    if request.method=="POST":
        print(1)
        name=request.POST.get('book')
        print(name)
        pdf=book_store.objects.filter(book_name=name)
        print(pdf)
        return render(request, 'pdf.html', {'books': pdf})

    return redirect('/explore')