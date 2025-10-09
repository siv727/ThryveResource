from django.conf import settings
from django.db import models

# Business Profile Model
class BusinessProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_business_profile')  # Unique related_name
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField()
    website_url = models.URLField(blank=True)

    def __str__(self):
        return self.company_name


# Profile Customization Model
class ProfileCustomization(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_profile_customization')  # Unique related_name
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    tagline = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.display_name
