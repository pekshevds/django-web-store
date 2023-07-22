from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
