from django.db import models

from playground.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=100, blank=True, null=False)
    content = models.TextField(blank=True, null=False)
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, related_name='posts', null=True)
