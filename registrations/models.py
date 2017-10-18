# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from datetime import datetime as dt


class Alumni(models.Model):
	fname = models.CharField("First Name", max_length=200, null=False, blank=False),
	mname = models.CharField("Middle Name", max_length=200, null=True, blank=True),
	lname = models.CharField("Last Name", max_length=200, null=False, blank=False),
	