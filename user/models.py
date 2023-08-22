from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from playground.models import BaseModel
from post.models import Like


class User(BaseModel, AbstractBaseUser):
    username = models.CharField(max_length=100, blank=True, null=False)

    USERNAME_FIELD = 'username'

    def like(self, post):
        Like.objects.create(post=post, user=self)
