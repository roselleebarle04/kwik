from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	user = models.OneToOneField(User)
	photo = models.ImageField('avatar', upload_to='avatar', default='avatar.jpeg')
	