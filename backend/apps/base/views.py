from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EventForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.base.models import Event, EventAttendance
from apps.accounts.models import Profile
from django.urls import reverse_lazy
class MainView(TemplateView):
    template_name = "base/index.html"


from .models import Event  # Make sure Event model is imported

class CreateEvent(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "base/create-event.html"
    success_url = reverse_lazy("base:main")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DiscoverEvent(TemplateView):
        template_name = "base/discover.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            events = Event.objects.select_related("created_by__profile").all()
            
            context['events'] = Event.objects.all().select_related("created_by")
            return context
class EventDetails(DetailView):
    model = Event
    template_name = "base/event-details.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()

        # Event creator profile
        context["creator_profile"] = getattr(event.created_by, "profile", None)

        # Check if current user has joined
        if self.request.user.is_authenticated:
            context["has_joined"] = EventAttendance.objects.filter(
                user=self.request.user, event=event
            ).exists()
        else:
            context["has_joined"] = False
        attendees = Profile.objects.filter(
            user__eventattendance__event=event
        ).select_related("user")
        # Get attendee profiles directly
        context["capacity"] = event.capacity
        context["attendees_count"] = attendees.count()
        context["attendees"] = attendees

        return context




@login_required
def join_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Save attendance if not exists
    EventAttendance.objects.get_or_create(
        user=request.user,
        event=event
    )

    # If event has Telegram link → redirect there
    if event.telegram:
        return redirect(event.telegram)

    # Else go back to event details
    return redirect("base:event_details", pk=event.id)
