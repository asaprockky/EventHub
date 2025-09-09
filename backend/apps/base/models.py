from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('gaming', 'Gaming'),
        ('study', 'Study Groups'),
        ('social', 'Social'),
        ('entertainment', 'Entertainment'),
        ('outdoor', 'Outdoor'),
        ('food', 'Food & Drinks'),
        ('arts', 'Arts & Culture'),
        ('fitness', 'Fitness & Wellness'),
        ('tech', 'Technology'),
    ]

    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    APPROVAL_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]

    title = models.CharField(max_length=200)
    telegram = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="base/event_images/", blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    attendees = models.ManyToManyField(User, through="EventAttendance", related_name="attended_events")

    max_attendees = models.PositiveIntegerField(default=50)
    min_age = models.PositiveIntegerField(blank=True, null=True)
    max_age = models.PositiveIntegerField(blank=True, null=True)
    gender_balance = models.CharField(max_length=20, default="any")

    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default="public")
    approval = models.CharField(max_length=10, choices=APPROVAL_CHOICES, default="automatic")
    capacity = models.PositiveIntegerField(default=20)

    special_requirements = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class EventAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "event")  # a user can’t join same event twice
