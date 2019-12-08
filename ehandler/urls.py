from django.urls import path, include
from django.conf.urls import url
from . import views as ehandler_views
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    UserEventListView
)

app_name = "ehandler"

urlpatterns = [
    path('', EventListView.as_view(), name='ehandler-home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(),
         name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('event/<int:pk>/attend/',
         ehandler_views.event_add_attendance, name='event-attend'),
    path('event/<int:pk>/cancel/',
         ehandler_views.event_cancel_attendance, name='event-cancel'),
    path('event/<int:pk>/help', ehandler_views.event_add_helper,
         name='event-help'),
    path('event/myevents/', UserEventListView.as_view(),
         name='user-event-list'),
    path('event/myevents/<int:pk>', ehandler_views.event_analysis,
         name='user-event-analysis'),
]
