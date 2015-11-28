from django.db import models
from accounts.models import Account
from .models import *


class Item(models.Model):
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	owner = models.ForeignKey(Account, null=True, blank=True)
	photo = models.ImageField('uploads', upload_to='uploads', default='uploads.jpeg')
	category = models.ForeignKey('Category')
	location = models.ForeignKey('Location')
	name = models.CharField(max_length = 100, null=True)
	description = models.CharField(max_length = 1000, null=True)
	unit_cost = models.FloatField(null=True, blank=True)
	quantity = models.PositiveIntegerField(null=True, blank=True)
	unit = models.CharField(max_length=10, null=True, default='pcs')
	
	def __unicode__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=100, null=True)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100, null=True)

	def __unicode__(self):
		return self.name