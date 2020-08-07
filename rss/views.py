from django.shortcuts import render


# Controller for displaying login page.
def login(request):
    return render(request, 'rss/login.html', {})
