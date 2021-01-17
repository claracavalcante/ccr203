from django.db import models

from ccr.apps.account.models import User
from ccr.apps.common.models import CoreModel


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(CoreModel):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)


class Comment(CoreModel):
    text = models.TextField()
    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE,
        blank=True, null=True)
    up_quantity = models.PositiveIntegerField(default=0, blank=True)
