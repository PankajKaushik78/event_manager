from django.shortcuts import render
from .models import Event


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'ehandler/home.html', context)
