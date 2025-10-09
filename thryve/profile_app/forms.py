from django import forms
from .models import BusinessProfile, ProfileCustomization

# Form for BusinessProfile
class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        exclude = ['user']  # Exclude 'user' field as it's set automatically in the view

# Form for ProfileCustomization
class ProfileCustomizationForm(forms.ModelForm):
    class Meta:
        model = ProfileCustomization
        exclude = ['user']  # Exclude 'user' field as it's set automatically in the view
