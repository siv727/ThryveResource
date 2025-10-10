from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the views module from auth_app to use the home view
from auth_app import views  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),  # Authentication URLs (formerly 'accounts/')
    path('profile/', include('profile_app.urls')),  # Profile URLs
    path('', views.home, name='home'),  # Home page route (linked to home view in auth_app)

    # You can add other URL patterns if necessary
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
