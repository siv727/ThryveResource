from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Get the custom user model dynamically
User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Attempt to get the user based on email using the custom user model
            user = User.objects.get(email=email)
            # Check the user's password
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
