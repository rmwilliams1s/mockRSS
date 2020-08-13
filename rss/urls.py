from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.render_feed, name='feed'),
    path('register/', views.Register.as_view(), name='register'),
]
