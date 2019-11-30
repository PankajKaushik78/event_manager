from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Event(models.Model):
    ename = models.CharField(max_length=100)
    econtent = models.TextField()
    edate = models.DateTimeField()
    eowner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
