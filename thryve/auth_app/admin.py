from django.contrib import admin
from profile_app.models import BusinessProfile, ProfileCustomization  # Correct import from profile_app

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'industry', 'website_url')  # Ensure fields exist in the model
    search_fields = ('company_name', 'industry')
    list_filter = ('industry',)

@admin.register(ProfileCustomization)
class ProfileCustomizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'tagline')  # Ensure fields exist in the model
    search_fields = ('display_name', 'tagline')
    list_filter = ('tagline',)
