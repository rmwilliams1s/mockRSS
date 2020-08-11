from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.feed, name='feed'),
    path('register', views.register, name='register')
]
