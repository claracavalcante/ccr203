from django.db import models

from ccr.apps.account.models import User
from ccr.apps.common.models import CoreModel


class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Challenge(CoreModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100, blank=True)
    deadline = models.DateField(null=True, blank=True)
    max_number_participants_per_team = models.PositiveIntegerField(
        default=4, blank=True)
    has_prizes = models.BooleanField(default=False, db_index=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    file_description = models.FileField(null=True, blank=True)
    youtube_url = models.URLField(blank=True)
    areas = models.ManyToManyField(Area, related_name='challenges', blank=True)


class Team(CoreModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(
        User, related_name='teams', blank=True)
    image = models.ImageField(null=True, blank=True)
    solution_file = models.FileField(null=True, blank=True)
    file_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    challenge = models.ForeignKey(
        Challenge, related_name='teams', on_delete=models.CASCADE,
        blank=True, null=True)
