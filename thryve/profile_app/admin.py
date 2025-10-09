from django.contrib import admin
from .models import BusinessProfile, ProfileCustomization  # Correct import from profile_app.models

# Register BusinessProfile with admin
@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'industry', 'website_url')  # Fields to display in list view
    search_fields = ('company_name', 'industry')  # Fields that can be searched in admin
    list_filter = ('industry',)  # Add a filter for the industry field

# Register ProfileCustomization with admin
@admin.register(ProfileCustomization)
class ProfileCustomizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'tagline')  # Fields to display in list view
    search_fields = ('display_name', 'tagline')  # Fields that can be searched in admin
    list_filter = ('tagline',)  # Add a filter for the tagline field
