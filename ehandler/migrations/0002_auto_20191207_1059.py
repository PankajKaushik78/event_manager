# Generated by Django 2.2.7 on 2019-12-07 10:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ehandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eattendees',
            field=models.ManyToManyField(related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='ecode',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='event',
            name='eenddate',
            field=models.DateField(default=datetime.datetime(2019, 12, 7, 10, 59, 12, 761019, tzinfo=utc), verbose_name='Event End date'),
        ),
        migrations.AddField(
            model_name='event',
            name='ehelpers',
            field=models.ManyToManyField(related_name='helpers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='econtent',
            field=models.TextField(verbose_name='Event Details'),
        ),
        migrations.AlterField(
            model_name='event',
            name='edate',
            field=models.DateField(verbose_name='Event Start date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='ename',
            field=models.CharField(max_length=100, verbose_name='Event Title'),
        ),
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