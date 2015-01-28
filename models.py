from django.db import models
from django.contrib.auth.models import Group
from django.conf import settings

# Create your models here.
class Content(models.Model):
    content = models.CharField(max_length=140)
    content_type = models.CharField(max_length=6)
    duration = models.IntegerField(min_value=1)
    start = models.DateTimeField()
    end = models.DateTimeField()
    rank = models.IntegerField(min_value=1)
    feed = models.ForeignKey(Feed)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Feed(models.Model):
    feedname = models.CharField(max_length=80)
    group = models.ForeignKey(Group)


class Screen(models.Model):
    screenname = models.CharField(max_length=80)
    hash = models.CharField(max_length=32)
    feeds = models.ManyToManyField(Feed)