from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),   # Login route #updated
    path('register/', views.register, name='register'),  # Register route
    path('logout/', views.logout, name='logout'),  # Logout route
    path('home/', views.home, name='home'),  # Home route (ensure you have a home view)
]
