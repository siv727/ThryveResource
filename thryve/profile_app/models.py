from django.conf import settings
from django.db import models

# BusinessProfile model
class BusinessProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL here
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    description = models.TextField()
    website_url = models.URLField(blank=True)  # Add website_url field here

    def __str__(self):
        return self.company_name


# ProfileCustomization model
class ProfileCustomization(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL here
    display_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    tagline = models.CharField(max_length=255, blank=True)  # Add tagline field here

    def __str__(self):
        return self.display_name
