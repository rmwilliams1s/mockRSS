from django.shortcuts import render
from django.utils import timezone
from .models import User
from .models import RSS


# Controller for displaying main page.
def login(request):
    feeds = RSS.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'rss/feed.html', {'feeds': feeds})
