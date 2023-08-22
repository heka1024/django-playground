from django.db import models

from playground.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=100, blank=True, null=False)
    content = models.TextField(blank=True, null=False)
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, related_name='posts', null=True)


class Like(BaseModel):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='likes', null=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='likes', null=False)

    class Meta:
        unique_together = ('post', 'user')


class Scrap(BaseModel):
    """
    Composite Primary Key 테스트

    post에 primary key = True가 걸려있지만 사실 primary key는 post와 user의 조합이다.
    장고가 Composite Primary Key를 지원하지 않기 때문
    """
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='scraps', null=False, primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='scraps', null=False)

    class Meta:
        models.UniqueConstraint(fields=['post', 'user'], name='unique_scrap')
