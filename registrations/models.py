# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from datetime import datetime as dt


class Alumni(models.Model):
	fname = models.CharField("First Name", max_length=200, null=False, blank=False),
	lname = models.CharField("Last Name", max_length=200, null=False, blank=False),
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=200, validators=[phone_regex], null=False, blank=False)
	email_regex = RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Invalid Email Format")
	email = models.CharField(max_length=200 ,validators=[email_regex], null=False, blank=False)
	gender = models.CharField("Gender" max_length=10, null=False, blank=False)
	dob = models.DateField("Date of Birth")