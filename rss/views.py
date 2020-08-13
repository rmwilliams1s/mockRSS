from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import RSS
import feedparser

def register(request):
    if request.GET.get("username") and request.GET.get("password"):
        name = request.GET['username']
        pwd = request.GET['password']
        user = User.objects.create_user(username=name, password=pwd)
        user.save()
        return redirect('rss/feed.html')
    else:
        return render(request, 'rss/register.html')


# Controller for displaying main page.
def render_feed(request):
    if request.GET.get("url"):
        url = request.GET["url"]
        feed = feedparser.parse(url)['feed']
        title = feed['title'] if 'title' in feed else ''
        date = feed['published'] if 'published' in feed else timezone.now()
        desc = feed['description'] if 'description' in feed else ''
        image = feed['image']['link'] if 'image' in feed else ''
        #user = request.user.id
        rss = RSS.objects.create(
            url=url, title=title, date=date, description=desc, image=image, user=User.id)
    else:
        feed = None
    #feeds = RSS.objects.get(user=request.user.id)
    return render(request, 'rss/feed.html', {'feeds': feed})
