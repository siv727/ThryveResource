from django.contrib import admin
from .models import BusinessProfile, ProfileCustomization

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'industry', 'website_url')

@admin.register(ProfileCustomization)
class ProfileCustomizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'tagline')
