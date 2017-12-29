# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class AlumniAdminSet(admin.ModelAdmin):

	actions_on_top = False
	actions_on_bottom = True
	list_filter = ('consul', 'entrep', 'govt', 'acadm', 'research', 'finance', 'info_tech', 'ques1','ques2','ques3','ques4','ques5','ques6')

	fieldsets = [
		('Personal Details', {'fields':['name', 'phone_no', 'email_id', 'gender', 'addrl1', 'addrl2', 'city', 'state', 'postal_code', 'country']}),
		('Education Details', {'fields':['degree', 'stream1', 'stream2', 'id_no', 'adm_year', 'grad_year']}),
		('Work Details', {'fields':['organisation', 'position', 'w_addrl1', 'w_addrl2', 'w_city']}),
		('Other Degree', {'fields':['oth_degr', 'oth_gradyear', 'oth_inst']}),
		('Previous Work Details (If Any)', {'fields':['p_organisation', 'p_position']}),
		('Expertise', {'fields':['consul', 'entrep', 'govt', 'acadm', 'research', 'finance', 'info_tech', 'other_exp']}),
		('I would be happy to', {'fields':['ques1','ques2','ques3','ques4','ques5','ques6','other_ques']}),
	]

admin.site.register(Alumni, AlumniAdminSet)
# admin.site.register(Alumni)