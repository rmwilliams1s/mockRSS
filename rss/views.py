from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import User, RSS, UserForm
import feedparser


# Controller for displaying login.
def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rss/feed.html')
    else:
        form = UserForm()
    return render(request, 'rss/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rss/feed.html', {'user': form})
    else:
        form = UserForm()
    return render(request, 'rss/register.html', {'form': form})


# Controller for displaying main page.
def render_feed(request):
    if request.GET.get("url"):
        # rss = RSS()
        url = request.GET["url"]
        feed = feedparser.parse(url)['feed']
        # rss.url = url
        # rss.title = feed['feed']['title'] if 'title' in feed else ''
        # rss.date = feed['feed']['published'] if 'published' in feed else timezone.now()
        # rss.description = feed['feed']['description'] if 'description' in feed else ''
        # rss.image = feed['feed']['image']['link'] if 'image' in feed else ''
        # rss.save()
    else:
        feed = None
    return render(request, 'rss/feed.html', {'feed': feed})
