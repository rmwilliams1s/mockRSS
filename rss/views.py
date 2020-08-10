from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User
from .models import RSS
from .forms import LoginForm


# Controller for displaying login.
def login(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = LoginForm(request.POST, instance=user)
        if form.is_valid():
            return redirect('rss/feed.html', pk=user.pk)
    else:
        form = LoginForm(instance=user)
    return render(request, 'rss/login.html', {'form': form})


# Controller for displaying main page.
def feed(request):
    feeds = RSS.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'rss/feed.html', {'feeds': feeds})
