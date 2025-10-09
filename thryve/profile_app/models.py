from django.db import models
from django.contrib.auth.models import User

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    company_name = models.CharField(max_length=120, blank=True)
    industry = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    address_line = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=120, blank=True)
    website_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.company_name or f"{self.user.username}'s business"


class ProfileCustomization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_customization')
    display_name = models.CharField(max_length=120, blank=True)
    tagline = models.CharField(max_length=160, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.display_name or self.user.get_username()
