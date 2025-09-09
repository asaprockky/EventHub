from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomSignupForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from apps.base.models import EventAttendance
from gemini import generate_bio
from django.utils.timesince import timesince
from django.utils import timezone
import datetime

# Create your views here.


class CustomLogin(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True 




class SignupView(generic.CreateView):
    form_class = CustomSignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("auth:login")



class ProfielView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        try:
            profile = Profile.objects.get(user=user)
            event_count = user.events.count()
            attended_events_count = EventAttendance.objects.filter(user=user).count()

            # Generate & save AI bio only if missing
            if not profile.bio:
                bio = generate_bio(profile.interests, profile.name, profile.age, profile.location)
                profile.bio = bio
                profile.save()
            else:
                bio = profile.bio

            # Convert comma-separated interests into a list
            profile.interests_list = profile.interests.split(",") if profile.interests else []

            # --- Recent activity ---
            activities = []

            # Created events
            created_events = user.events.order_by('-created_at')[:5]
            for event in created_events:
                activities.append({
                    "icon": "fas fa-plus",
                    "message": f'Created "{event.title}"',
                    "time": f'{timesince(event.created_at)} ago',
                    "datetime": event.created_at
                })

            # Attended events
            attended = EventAttendance.objects.filter(user=user).order_by('-joined_at')[:5]
            for att in attended:
                activities.append({
                    "icon": "fas fa-check",
                    "message": f'Attended "{att.event.title}"',
                    "time": f'{timesince(att.joined_at)} ago',
                    "datetime": att.joined_at
                })

            # Received reviews
            rated_events = EventAttendance.objects.filter(event__created_by=user, rating__isnull=False).order_by('-joined_at')[:5]
            for att in rated_events:
                activities.append({
                    "icon": "fas fa-star",
                    "message": f'Received {att.rating}-star review for "{att.event.title}"',
                    "time": f'{timesince(att.joined_at)} ago',
                    "datetime": att.joined_at
                })

            # Sort by actual datetime descending
            activities.sort(key=lambda x: x['datetime'], reverse=True)
            for act in activities:
                act.pop("datetime")  # remove datetime before sending to template

            # --- Hosted events ---
            hosted_events = user.events.all().order_by('-created_at')
            events_data = []
            now = timezone.now()

            for event in hosted_events:
                joined_count = event.attendees.count()
                max_count = event.max_attendees or 20

                # Determine status
                event_datetime = timezone.make_aware(
                    datetime.datetime.combine(event.date, event.time)
                )
                if now < event_datetime:
                    status = "Will Start"
                elif now >= event_datetime:
                    status = "Active"
                # Optional: add "Finished" logic if needed

                events_data.append({
                    "title": event.title,
                    "date": event.date,
                    "joined_count": joined_count,
                    "max_count": max_count,
                    "status": status,
                    "icon": "fas fa-football-ball",  # optional placeholder
                })

            # Add everything to context
            context["profile"] = profile
            context["ai_bio"] = bio
            context["event_count"] = event_count
            context["attended_events_count"] = attended_events_count
            context["activities"] = activities
            context["hosted_events"] = events_data

        except Profile.DoesNotExist:
            context["profile"] = None
            context["ai_bio"] = None
            context["activities"] = []
            context["hosted_events"] = []

        return context