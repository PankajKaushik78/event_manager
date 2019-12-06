# Generated by Django 2.2.7 on 2019-12-05 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ehandler', '0002_event_ecode'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_registered', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehandler.Event', verbose_name='Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Attendee')),
            ],
            options={
                'verbose_name': 'Attendee for event',
                'verbose_name_plural': 'Attendees for events',
                'ordering': ['time_registered'],
                'unique_together': {('event', 'user')},
            },
        ),
    ]
