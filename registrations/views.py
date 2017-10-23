# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

from datetime import datetime as dt

# Create your views here.

def index(request):
	return render(request, './registrations/index.html')

def alumni_register(request, pk):
	post
	if request.POST:
		print request.POST
		pst = request.POST
		name = pst['fname'].strip() + " " + pst['lname'].strip()
		gender = pst['gender']
		if gender == "Male":
			gender = "M"
		elif gender == "Female":
			gender = "F"
		phone_no = int(pst['phone_no'])
		email_id = pst['email_id'].lower().strip()
		dob_s = pst['dob'].strip()
		dob = dt.strptime(dob_s, "%Y-%m-%d").date()
		addrl1 = pst['address-line1'].strip()
		addrl2 = pst['address-line2'].strip()
		state = pst['region'].strip()
		postcode = int(pst['postalcode'])
		country = pst['country']

		# Work details
		organisation = pst['organisation']
		position = pst['position']
		w_addrl1 = pst['w_address-line1']
		w_addrl2 = pst['w_address-line2']
		w_city = pst['w_city']
		w_region = pst['w_region']
		w_postcode = int(pst['w_postcode'])
		w_country = pst['w_country']


		registered_alumni = Alumni.objects.all()
		list_of_registered_emails = [x.email_id for x in registered_alumni]

		if email_id in list_of_registered_emails:
			return render(request, 'register.html', {'status':0, 'message':"This email is already registered. Please try again."})
		else:
			alumni = Alumni()
			alumni.name = name
			alumni.gender = gender
			alumni.phone_no = phone_no
			alumni.email_id = email_id
			alumni.dob = dob
			alumni.addrl1 = addrl1
			alumni.addrl2 = addrl2
			alumni.state = state
			alumni.postcode = postcode
			alumni.country = country

			alumni.organisation = organisation
			alumni.position = position
			alumni.w_addrl1 = w_addrl1
			alumni.w_addrl2 = w_addrl2
			alumni.w_city = w_city
			alumni.w_postcode = w_postcode
			alumni.w_country = w_country
			