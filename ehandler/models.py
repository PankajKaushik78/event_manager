from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from ehandler.utils import unique_event_code_generator
# Create your models here.


class Event(models.Model):
    ename = models.CharField(max_length=100)
    econtent = models.TextField()
    edate = models.DateTimeField()
    eowner = models.ForeignKey(User, on_delete=models.CASCADE)
    ecode = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

# class Attendee(models.Model):
#     event = models.ManyToManyField(Event, on_delete=models.CASCADE)
#     attendee = models.ForeignKey(User, on_delete=models.CASCADE)


# Code for generating unique event code and saving it in Event.ecode
def pre_save_create_event_code(sender, instance, *args, **kwargs):
    if not instance.ecode:
        instance.ecode = unique_event_code_generator(instance)


pre_save.connect(pre_save_create_event_code, sender=Event)
