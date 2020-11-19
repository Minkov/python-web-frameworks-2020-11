from django.contrib.auth.models import User
from django.db import models


class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(
        upload_to='pythons',
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
