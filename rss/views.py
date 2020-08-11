from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from .models import RSS
from .forms import UserForm


# Controller for displaying login.
def login(request):
    #user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect('rss/feed.html')
    else:
        form = UserForm()
    return render(request, 'rss/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rss/feed.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'rss/register.html', {'form': form})


# Controller for displaying main page.
def feed(request):
    feeds = RSS.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'rss/feed.html', {'feeds': feeds})
