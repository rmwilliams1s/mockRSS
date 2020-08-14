from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_feed, name='feed'),
    path('register/', views.Register.as_view(), name='register'),
]
