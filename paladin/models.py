from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.


class Query(models.Model):
	text = models.CharField(max_length=60)
	
	def __str__(self):
		return self.text


class Result(models.Model):
	channelId = models.CharField(max_length=30)
	channelTitle = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	publishedAt = models.DateField()
	url = models.CharField(max_length=30)
	title = models.CharField(max_length=60)
	videoId = models.CharField(max_length=30)

	def __str__(self):
		return self.title