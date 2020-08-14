from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RSS, SortFeedForm
import feedparser
from datetime import datetime


# Controller for registration page
class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


# Controller for displaying main page
def render_feed(request):
    if request.GET.get("url"):
        url = request.GET["url"]
        feed = feedparser.parse(url)
        for post in feed.entries:
            title = post['title'] if 'title' in post else ''
            link = post['link'] if 'link' in post else ''

            if 'published' in post:
                date_str = post['published']
            elif 'updated' in post:
                date_str = post['updated']
            # change string -> datetime obj
            formats = ["%a, %d %b %Y %H:%M %Z", "%a, %d %b %Y %H:%M:%S %z"]
            for str_form in formats:
                try:
                    date = datetime.strptime(date_str, str_form)
                except ValueError:
                    if formats.index(str_form) == len(formats)-1:
                        date = datetime.min
                    else:
                        continue
                
            if 'description' in post:
                desc = post['description']
            elif 'subtitle' in post:
                desc = post['subtitle']
            else:
                desc = ''

            image = ''

            if 'image' in post:
                image = post['image']['link']  
            elif 'media_content' in post:
                if len(post['media_content']) > 0 and 'url' in post['media_content'][0]:
                    # Just grab first image from resources
                    image = post['media_content'][0]['url']
            elif 'media_thumbnail' in post:
                if len(post['media_thumbnail']) > 0 and 'url' in post['media_thumbnail'][0]:
                    # Just grab first image from thumbnails
                    image = post['media_thumbnail'][0]['url']
            elif 'links' in post:
                for link in post['links']:
                    if 'image' in link['type']:
                        image = link['href'] 

            user = request.user
            rss = RSS.objects.create(
                url=link, title=title, date=date, description=desc, image=image, user=user)
            rss.save()
    else:
        feed = None

    # display all feeds associated with current user
    feeds = RSS.objects.filter(user=request.user)

    if request.method == "POST":
        sort_form = SortFeedForm(request.POST)
        # add given sort query
        if sort_form.is_valid():
            sort = sort_form.cleaned_data['choice']
            if sort == 'date_desc':
                feeds = feeds.order_by('-date')
            elif sort == 'date_asc':
                feeds = feeds.order_by('date')
            elif sort == 'title_asc':
                feeds = feeds.order_by('title')
            elif sort == 'title_desc':
                feeds = feeds.order_by('-title')
            else: # sort == 'description'
                keyword = sort_form.cleaned_data['keyword']
                feeds = feeds.filter(description__contains=keyword)
            return render(request, 'feed.html', {'feeds': feeds, 'sort_form': sort_form})
    else:
        sort_form = SortFeedForm()

    return render(request, 'feed.html', {'feeds': feeds, 'sort_form': sort_form})
