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
	
