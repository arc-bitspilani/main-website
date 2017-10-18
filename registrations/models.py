# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

from datetime import datetime as dt

from countries import *


class Alumni(models.Model):
	GENDERS = (
		('M', 'Male'),
		('F', 'Female'),
	)
	user = models.OneToOneField(User, null=True, blank=True)
	fname = models.CharField("First Name", max_length=200),
	lname = models.CharField("Last Name", max_length=200),
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=200, validators=[phone_regex])
	# email_regex = RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Invalid Email Format")
	email = models.EmailField()
	gender = models.CharField(max_length=1, choices=GENDERS)
	dob = models.DateField("Date of Birth")
	addrl1 = models.CharField("Address Line 1", max_length=200)
	addrl2 = models.CharField("Address Line 2", max_length=200, null=True, blank=True)
	city = models.CharField("City", max_length=30)
	state = models.CharField("State/Province/Region", max_length=50)
	postcode = models.BigIntegerField()
	country = models.CharField("Country", max_length=5)

	verified = models.NullBooleanField(default=False)