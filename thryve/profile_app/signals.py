from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BusinessProfile, ProfileCustomization

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        BusinessProfile.objects.create(user=instance)
        ProfileCustomization.objects.create(user=instance)
