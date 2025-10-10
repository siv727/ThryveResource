from django.urls import path
from . import views

urlpatterns = [
    path('business/', views.business_profile_view, name='business_profile'),
    path('customize/', views.profile_customization_view, name='profile_customization'),
]
