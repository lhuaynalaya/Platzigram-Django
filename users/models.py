# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	website = models.URLField(max_length=200, blank=True)
	biography = models.TextField(blank=True)
	phone_numer = models.CharField(max_length=20, blank=True)
	picture = models.ImageField(upload_to='users/picture', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username
		
