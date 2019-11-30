from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ehandler-home'),
]
