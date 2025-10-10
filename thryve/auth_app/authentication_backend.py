from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Attempt to get the user based on email
            user = User.objects.get(email=email)
            # Check the user's password
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
