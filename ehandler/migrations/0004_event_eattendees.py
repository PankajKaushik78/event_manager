# Generated by Django 2.2.7 on 2019-12-05 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ehandler', '0003_eventregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eattendees',
            field=models.ManyToManyField(related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
    ]