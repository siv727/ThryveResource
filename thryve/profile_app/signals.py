from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BusinessProfile, ProfileCustomization

@receiver(post_save, sender=User)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        BusinessProfile.objects.create(user=instance)
        ProfileCustomization.objects.create(user=instance)
