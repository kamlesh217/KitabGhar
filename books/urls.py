from django.contrib import admin
from django.urls import path,include
from books import views

urlpatterns = [
    path('',views.home, name="home"),
    path('explore/',views.explore, name="explore"),
    path('collection/',views.collection, name="collection"),
   #path('collection/explore/',views.explore, name="explore"),
    #path('explore/collection/',views.collection, name="collection"),
]