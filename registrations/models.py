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
	name = models.CharField("Name", max_length=200)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_no = models.CharField(max_length=200, validators=[phone_regex])
	# email_regex = RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Invalid Email Format")
	email_id = models.EmailField()
	gender = models.CharField(max_length=1, choices=GENDERS)
	dob = models.DateField("Date of Birth")
	addrl1 = models.CharField("Address Line 1", max_length=200)
	addrl2 = models.CharField("Address Line 2", max_length=200, null=True, blank=True)
	city = models.CharField("City", max_length=30)
	state = models.CharField("State/Province/Region", max_length=50)
	postcode = models.BigIntegerField()
	country = models.CharField("Country", max_length=5)

	verified = models.NullBooleanField(default=False)

	# Education Details
	branch = models.CharField("Branch", max_length=50)
	stream1 = models.CharField("Stream 1", max_length=100)
	stream2 = models.CharField("Stream 2", max_length=100, null=True, blank=True)
	id_no = models.CharField("ID No.", max_length=15)
	adm_year = models.PositiveIntegerField("Admission Year")
	grad_year = models.PositiveIntegerField("Graduation Year")
	
	# Work Details
	organisation = models.CharField("Organisation", max_length=200)
	position = models.CharField("Position", max_length=200)
	w_addrl1 = models.CharField("Work Address Line 1", max_length=200)
	w_addrl2 = models.CharField("Work Address Line 2", max_length=200)
	w_city = models.CharField("Work City", max_length=200)
	w_region = models.CharField("Work State/Province/Region", max_length=200)
	w_postcode = models.BigIntegerField(default=0)
	w_country = models.CharField("Work Country", max_length=200)

	# Previous Work Details
	p_organisation = models.CharField("Organisation", max_length=200, null=True, blank=True)
	p_position = models.CharField("Position", max_length=200, null=True, blank=True)
	p_w_addrl1 = models.CharField("Work Address Line 1", max_length=200, null=True, blank=True)
	p_w_addrl2 = models.CharField("Work Address Line 2", max_length=200, null=True, blank=True)
	p_w_city = models.CharField("Work City", max_length=200, null=True, blank=True)
	p_w_region = models.CharField("Work State/Province/Region", max_length=200, null=True, blank=True)
	p_w_postcode = models.BigIntegerField(default=0, null=True, blank=True)
	p_w_country = models.CharField("Work Country", max_length=200, null=True, blank=True)

	class Meta:
		verbose_name = "Alumni"
		verbose_name_plural = "Alumni"

	def __str__(self):
		return self.name