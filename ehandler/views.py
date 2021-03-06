from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse
from .models import Event, EventRegistration
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
# from .forms import CodeCheckForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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

# View for analysis of a particular event


def event_analysis(request, pk):
    event = Event.objects.get(pk=pk)
    attendees = event.eattendees.all()
    helpers = event.ehelpers.all()
    total_attendees = event.eattendees.all().count()
    total_helpers = event.ehelpers.all().count()
    context = {
        'event': event,
        'attendees': attendees,
        'helpers': helpers,
        'total_attendees': total_attendees,
        'total_helpers': total_helpers,
    }
    return render(request, 'ehandler/event_analysis.html', context)


@login_required
def event_add_attendance(request, pk):
    try:
        this_event = Event.objects.get(pk=pk)
        if request.method == 'POST':
            # form = CodeCheckForm(request.POST)
            code = request.POST.get('code')
            if code == this_event.ecode:
                user = request.user
                # this_event = Event.objects.get(pk=pk)
                this_event.add_user_to_list_of_attendees(user=user)
                this_event.eattendees.add(user)
                messages.success(
                    request, f'You have been added to attendee list of {this_event.ename}')
                return redirect("ehandler:event-detail", pk=pk)
            elif code != this_event.ecode:
                messages.warning(
                    request, f'Please enter the correct event code')
                return redirect("ehandler:event-detail", pk=pk)
        # else:
        #     form = CodeCheckForm()
        return render(request, "ehandler/event_detail.html")

    except IntegrityError:
        messages.add_message(request, messages.INFO,
                             "You are already in the attendee list")
        return redirect("ehandler:event-detail", pk=pk)


@login_required
def event_cancel_attendance(request, pk):
    try:
        user = request.user
        this_event = Event.objects.get(pk=pk)
        this_event.remove_user_from_list_of_attendees(request.user)
        this_event.eattendees.remove(user)
        messages.warning(
            request, f'You have been removed from attendee list of {this_event.ename}!')
        return redirect("ehandler:event-detail", pk=pk)
    except Exception:
        messages.add_message(request, messages.INFO,
                             "You are not in the attendee list")
        return redirect("ehandler:event-detail", pk=pk)


@login_required
def event_add_helper(request, pk):
    # try:
    user = request.user
    this_event = Event.objects.get(pk=pk)
    this_event.ehelpers.add(user)
    messages.success(
        request, f'Thanks for helping in organising {this_event.ename}! We will contact you soon')
    return redirect("ehandler:event-detail", pk=pk)


class UserEventListView(ListView, LoginRequiredMixin):
    model = Event
    template_name = 'ehandler/event_myevents.html'
    context_object_name = 'events'
    ordering = ['-edate']


class EventListView(ListView):
    model = Event
    template_name = 'ehandler/home.html'
    context_object_name = 'events'
    ordering = ['-edate']


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['ename', 'econtent', 'edate', 'eenddate']

    def form_valid(self, form):
        form.instance.eowner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("ehandler:event-detail", kwargs={'pk': self.object.pk})


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['ename', 'econtent', 'edate', 'eenddate']

    def form_valid(self, form):
        form.instance.eowner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.eowner:
            return True
        return False

    def get_success_url(self):
        return reverse("ehandler:event-detail", kwargs={'pk': self.object.pk})


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.eowner:
            return True
        return False


# def event_join_code(request):
#     # if request.method == 'POST':
#     #     code = request.POST.get('code')
#     #     event_codes = Event.objects.values_list('ecode', flat=True)
#     #     if code in event_codes:
#     #         user = request.user
#     #         this_event = Event.objects.get(ecode=code)
#     #         this_event.add_user_to_list_of_attendees(user=user)
#     #         this_event.eattendees.add(user)
#     #         messages.success(
#     #             request, f'You have been added to attendee list of {this_event.ename}')
#     #         return redirect("ehandler:event-detail", pk=this_event.pk)
#     #     elif code != this_event.ecode:
#     #         messages.warning(
#     #             request, f'Please enter the correct event code')
#     #         return redirect("ehandler:event-join-code")
#     return render(request, "ehandler/event_join_code.html")
