from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title","telegram", "description", "category", "image",
            "date", "time", "location", "max_attendees",
            "min_age", "max_age", "gender_balance",
            "visibility", "approval", "special_requirements",
        ]
