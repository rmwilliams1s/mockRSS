from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/success', views.feed, name='feed')
]
