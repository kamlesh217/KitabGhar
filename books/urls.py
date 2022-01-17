from django.contrib import admin
from django.urls import path,include
from books import views

urlpatterns = [
    path('',views.home, name="home"),
    path('explore/',views.explore, name="explore"),
    path('collection/',views.collection, name="collection"),
    path('register/',views.register, name="register"),
    path('register/register',views.register, name="register"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('account/',views.account, name='account'),
    path('logout',views.logoutuser, name='logout'),
    path('remove',views.remove,name='remove'),
    path('comment',views.comment,name='comment'),
    path('add',views.explore,name='add'),
]