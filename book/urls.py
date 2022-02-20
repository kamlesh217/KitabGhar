from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.login_user, name="login"),
    path('explore/',views.explore, name="explore"),
    path('register/',views.register, name="register"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('account/',views.account, name='account'),
    path('logout/',views.logout_user, name='logout'),
    path('comment',views.comment,name='comment'),
]
