from django.shortcuts import render
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'ehandler/home.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'ehandler/home.html'
    context_object_name = 'events'
    ordering = ['-edate']


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['ename', 'econtent', 'edate']

    def form_valid(self, form):
        form.instance.eowner = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['ename', 'econtent', 'edate']

    def form_valid(self, form):
        form.instance.eowner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.eowner:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.eowner:
            return True
        return False
