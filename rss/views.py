from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User, RSS, UserForm
import feedparser


# Controller for displaying login.
def login(request):
    # user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rss/feed.html', {'user': form})
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
def render_feed(request, user):
    feeds = RSS.objects.filter(date__lte=timezone.now()).order_by('date')
    if request.GET.get("url"):
        url = request.GET["url"]
        feed_temp = RSS(request.GET)
        if feed_temp.is_valid():
            info = feedparser.parse(url)
            feed = feed_temp.save(commit=False)
            feed.url = url
            feed.title = info['feed']['title']
            feed.date = info['feed']['published']
            feed.description = info['feed']['description']
            feed.user = user
            if 'image' in info:
                feed.image = info['feed']['image']['link']
            feed.save()
            return redirect('rss/feed.html', {'user': user})
    return render(request, 'rss/feed.html', {'user': user, 'feeds': feeds})