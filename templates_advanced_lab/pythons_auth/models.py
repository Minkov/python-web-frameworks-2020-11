from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    date_of_birth = models.DateTimeField()
    profile_image = models.ImageField(
        upload_to="profiles/"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)