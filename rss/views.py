from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RSS
import feedparser
import datetime


class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


# Controller for displaying main page.
def render_feed(request):
    if request.GET.get("url"):
        url = request.GET["url"]
        feed = feedparser.parse(url)['feed']
        print(feed)
        title = feed['title'] if 'title' in feed else ''
        link = feed['link'] if 'link' in feed else ''

        if 'published' in feed:
            date = feed['published']
        elif 'updated' in feed:
            date = feed['updated']
        else: 
            date = datetime.MINYEAR

        if 'description' in feed:
            desc = feed['description']
        elif 'subtitle' in feed:
            desc = feed['subtitle']
        else:
            desc = ''
            
        image = feed['image']['link'] if 'image' in feed else ''
        user = request.user
        rss = RSS.objects.create(
            url=link, title=title, date=date, description=desc, image=image, user=user)
        rss.save()
    else:
        feed = None
    feeds = RSS.objects.filter(user=request.user)
    return render(request, 'feed.html', {'feeds': feeds})
