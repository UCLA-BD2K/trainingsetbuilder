from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publication(models.Model):
	pmid = models.CharField(max_length=10, primary_key=True)
	classification = models.IntegerField(default=-1)
	# -1 unclassified
	# 0 no tool
	# 1 tool
	# 2 ambiguous
	def __str__(self):
		return self.pmid
	def classified(self):
		return classification != -1
