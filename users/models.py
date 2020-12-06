from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    posts_count = models.PositiveIntegerField(null=True, blank=True)
