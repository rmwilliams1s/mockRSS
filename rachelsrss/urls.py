from django.contrib import admin
from django.urls import path, include
from rss.views import render_feed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rachelsrss/', include('rss.urls')),
    path('rachelsrss/', include('django.contrib.auth.urls')),
    path('', render_feed, name='feed'),
]
