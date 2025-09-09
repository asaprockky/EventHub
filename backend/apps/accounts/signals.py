from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, ProfileRating


from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()



@receiver([post_save, post_delete], sender=ProfileRating)
def update_profile_rating(sender, instance, **kwargs):
    profile = instance.profile
    avg = profile.ratings.aggregate(Avg("score"))["score__avg"] or 0
    profile.rating = avg
    profile.save(update_fields=["rating"])