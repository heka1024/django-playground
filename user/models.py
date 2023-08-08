from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from playground.models import BaseModel


class User(BaseModel, AbstractBaseUser):
    username = models.CharField(max_length=100, blank=True, null=False)
