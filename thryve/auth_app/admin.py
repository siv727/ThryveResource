from django.contrib import admin
from profile_app.models import BusinessProfile, ProfileCustomization  # Import from profile_app

# Remove the registration code from auth_app/admin.py
# No need to register BusinessProfile and ProfileCustomization here, it should be in profile_app/admin.py
