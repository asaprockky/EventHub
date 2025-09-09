# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomSignupForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    location = forms.CharField(max_length=100, required=True)
    interests = forms.MultipleChoiceField(
        choices=[
            ("sports", "Sports"),
            ("gaming", "Gaming"),
            ("study", "Study"),
            ("social", "Social"),
            ("entertainment", "Entertainment"),
            ("outdoor", "Outdoor"),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "age", "location", "interests")

    def save(self, commit=True):
        user = super().save(commit=False)  # don’t save yet
        if commit:
            user.save()  # explicitly save user first
            interests_str = ",".join(self.cleaned_data["interests"])
            Profile.objects.create(
                user=user,
                age=self.cleaned_data["age"],
                location=self.cleaned_data["location"],
                interests=interests_str,
            )
        return user

