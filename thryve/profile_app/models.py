from django.conf import settings
from django.db import models

class BusinessProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='business_profile')  # Add related_name here
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField()
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.company_name


class ProfileCustomization(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_customization')  # Add related_name here
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    tagline = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.display_name
