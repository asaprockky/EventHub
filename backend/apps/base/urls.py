from django.urls import path
from .views import MainView,CreateEvent, DiscoverEvent, EventDetails, join_event

app_name = "base"

urlpatterns = [
    path("main", MainView.as_view(), name="main"),
    path("create-event", CreateEvent.as_view(), name="create_event"),
    path("discover", DiscoverEvent.as_view(), name="discover"),
    path("event/<int:pk>/", EventDetails.as_view(), name="event_details"),
    path("events/<int:event_id>/join/", join_event, name="join_event"),
]
