from django.db import models

# Create your models here.
class Content (models.Model):
	content = models.CharField(max_length=140)
	content_type = models.CharField(max_length=6)
	duration = models.IntegerField(min_value=1)
	start = models.DateTimeField()
	end = models.DateTimeField()
	rank = models.IntegerField(min_value=1)
	#feed = models.ForeignKey()
	#user = models.ForeignKey()
	
class Feed (models.Model):
	feedname = models.CharField(max_length=80)
	
class Screen (models.Model):
	screenname = models.CharField(max_length=80)
	hash = models.CharField(max_length=32)
	
