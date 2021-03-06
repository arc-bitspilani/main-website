# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

from datetime import datetime as dt

from countries import *

DEG_CHOICES = (
	('Single Degree (B.E.)','Single Degree (B.E.)'),
	('Dual Degree (MSc and B.E.)','Dual Degree (MSc and B.E.)'),
	('B.Pharma','B.Pharma'),
	('M.E.','M.E.'),
	('Msc. Tech.','Msc. Tech.'),
	('PhD','PhD'),
	('MBA','MBA'),
	('MS','MS'),
	('M.tech','M.tech'),
	('MMS','MMS'),
)


class Alumni(models.Model):
	GENDERS = (
		('M', 'Male'),
		('F', 'Female'),
	)
	user = models.OneToOneField(User, null=True, blank=True)
	name = models.CharField("Name", max_length=200)
	# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_no = models.CharField(max_length=200)
	# email_regex = RegexValidator(regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", message="Invalid Email Format")
	email_id = models.EmailField()
	gender = models.CharField(max_length=1, choices=GENDERS)
	# dob = models.DateField("Date of Birth")
	addrl1 = models.CharField("Address Line 1", max_length=200)
	addrl2 = models.CharField("Address Line 2", max_length=200, null=True, blank=True)
	city = models.CharField("City", max_length=30)
	state = models.CharField("State/Province/Region", max_length=50, null=True, blank=True)
	postal_code = models.CharField("Postal Code", max_length=20)
	# postcode = models.BigIntegerField()
	country = models.CharField("Country", max_length=5, default="India")

	# verified = models.NullBooleanField(default=False)

	# Education Details
	degree = models.CharField("Degree", max_length=50, choices=DEG_CHOICES)
	stream1 = models.CharField("Stream 1", max_length=100)
	stream2 = models.CharField("Stream 2 (If Any)", max_length=100, null=True, blank=True)
	id_no = models.CharField("ID No.", max_length=15, null=True, blank=True)
	adm_year = models.PositiveIntegerField("Admission Year", default=1988)
	grad_year = models.PositiveIntegerField("Graduation Year")

	# Other Degree
	oth_degr = models.CharField("Other Degree", max_length=200, null=True, blank=True)
	oth_gradyear = models.PositiveIntegerField("Year of Completion", null=True, blank=True)
	oth_inst = models.CharField("Institution Name", max_length=500, null=True, blank=True)
	
	# Work Details
	organisation = models.CharField("Organisation", max_length=200)
	position = models.CharField("Position", max_length=200)
	w_addrl1 = models.CharField("Address Line 1", max_length=200, null=True, blank=True)
	w_addrl2 = models.CharField("Address Line 2", max_length=200, null=True, blank=True)
	w_city = models.CharField("City", max_length=200, null=True, blank=True)
	# w_region = models.CharField("Work State/Province/Region", max_length=200)
	# w_postcode = models.BigIntegerField("Work Postcode")
	# w_country = models.CharField("Work Country", max_length=200)

	# Previous Work Details
	p_organisation = models.CharField("Organisation", max_length=200, null=True, blank=True)
	p_position = models.CharField("Position", max_length=200, null=True, blank=True)
	p_w_addrl1 = models.CharField("Work Address Line 1", max_length=200, null=True, blank=True)
	p_w_addrl2 = models.CharField("Work Address Line 2", max_length=200, null=True, blank=True)
	p_w_city = models.CharField("Work City", max_length=200, null=True, blank=True)
	p_w_region = models.CharField("Work State/Province/Region", max_length=200, null=True, blank=True)
	p_w_postcode = models.BigIntegerField(null=True, blank=True)
	p_w_country = models.CharField("Work Country", max_length=200, null=True, blank=True)

	consul = models.BooleanField("Consultancy")
	entrep = models.BooleanField("Entrepreneurship")
	govt = models.BooleanField("Government")
	acadm = models.BooleanField("Academia")
	research = models.BooleanField("Research")
	finance = models.BooleanField("Finance")
	info_tech = models.BooleanField("Information Technology")
	other_exp = models.CharField("Other", max_length=200, null=True, blank=True);

	ques1 = models.BooleanField("help BITS identify and recruit from India or elsewhere.")
	ques2 = models.BooleanField("collaborate on research with BITS faculty.")
	ques3 = models.BooleanField("identify and create new industry focused post graduate programs to be run by BITS.")
	ques4 = models.BooleanField("help BITS grow its off-campus programs (Work Integrated Learning Programs, Practice Schools).")
	ques5 = models.BooleanField("happy to facilitate BITS' faculty spending few weeks as visiting interns.")
	ques6 = models.BooleanField("consider donating funds for the creation of infrastructure/research/faculty enrichment/student enrichment.")

	other_ques = models.CharField("Other", max_length=500, null=True,blank=True)

	class Meta:
		verbose_name = "Alumni"
		verbose_name_plural = "Alumni"

	def __str__(self):
		return self.name