from django.db import models

from ccr.apps.account.models import User
from ccr.apps.common.models import CoreModel


class Meeting(CoreModel):
    mentor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mentor', blank=True, null=True)
    mentee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='mentee', blank=True, null=True)

    mentor_comments = models.TextField(blank=True)
    mentee_comments = models.TextField(blank=True)

    deadline = models.DateTimeField(blank=True)
