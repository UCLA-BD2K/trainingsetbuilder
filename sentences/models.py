from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sentence(models.Model):
	text = models.CharField(max_length=500, default="none")
	positive = models.BooleanField(default=False)
	def __str__(self):
		return self.text
