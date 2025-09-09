from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username



class ProfileRating(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="ratings")
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()  # e.g., 1–5 stars
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("profile", "rated_by")  # prevent duplicate ratings



