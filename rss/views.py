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
        feed = feedparser.parse(url)
        for post in feed.entries:
            title = post['title'] if 'title' in post else ''
            link = post['link'] if 'link' in post else ''

            if 'published' in post:
                date = post['published']
            elif 'updated' in post:
                date = post['updated']
            else: 
                date = datetime.MINYEAR

            if 'description' in post:
                desc = post['description']
            elif 'subtitle' in post:
                desc = post['subtitle']
            else:
                desc = ''

            if 'image' in post:
                image = post['image']['link']  
            elif 'media_content' in post:
                # Just grab first image from resources
                image = post['media_content'][0]['url']
            elif 'links' in post:
                for link in post['links']:
                    if 'image' in link['type']:
                        image = link['href'] 
            else: 
                image = ''
            user = request.user
            rss = RSS.objects.create(
                url=link, title=title, date=date, description=desc, image=image, user=user)
            rss.save()
    else:
        feed = None
    feeds = RSS.objects.filter(user=request.user)
    return render(request, 'feed.html', {'feeds': feeds})
