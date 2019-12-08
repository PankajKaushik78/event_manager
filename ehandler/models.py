from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.db.models.signals import pre_save
from ehandler.utils import unique_event_code_generator
from django.utils import timezone


# Event model contains all the info of a particular event
class Event(models.Model):
    ename = models.CharField(max_length=100, verbose_name="Event Title")
    econtent = models.TextField(verbose_name="Event Details")
    edate = models.DateTimeField(verbose_name="Event Start date (YY-MM-DD)")
    eenddate = models.DateTimeField(
        verbose_name="Event End date (YY-MM-DD)")
    eowner = models.ForeignKey(User, on_delete=models.CASCADE)
    eattendees = models.ManyToManyField(
        User, related_name='attendees')
    ecode = models.CharField(max_length=120, blank=True)
    ehelpers = models.ManyToManyField(User, related_name='helpers')

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def get_registrations(self):
        return EventRegistration.objects.filter(event=self)

    def add_user_to_list_of_attendees(self, user):
        registration = EventRegistration.objects.create(user=user,
                                                        event=self,
                                                        time_registered=timezone.now())

    def remove_user_from_list_of_attendees(self, user):
        registration = EventRegistration.objects.get(user=user, event=self)
        registration.delete()


# This model relates attendees with the event
class EventRegistration(models.Model):
    # 'user' corresponds to the attendee of the event
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Attendee')
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, verbose_name="Event")
    time_registered = models.DateTimeField()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Attendee for event'
        verbose_name_plural = 'Attendees for events'
        ordering = ['time_registered', ]
        unique_together = ('event', 'user')

    def save(self, *args, **kwargs):
        if self.id is None and self.time_registered is None:
            self.time_registered = datetime.datetime.now()
        super(EventRegistration, self).save(*args, **kwargs)


# Code for generating unique event code and saving it in Event.ecode
def pre_save_create_event_code(sender, instance, *args, **kwargs):
    if not instance.ecode:
        instance.ecode = unique_event_code_generator(instance)


pre_save.connect(pre_save_create_event_code, sender=Event)
