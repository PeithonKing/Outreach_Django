import sys
import os
import django

sys.path.append('Outreach')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Outreach.settings'
django.setup()

from main.models import Coordinators as c

p=[
	{
		"name" : "Debashish Jena",
		"year" : 2016,
		"picture" : "static/student_coordinators/debashish.jpg"},
	{
		"name" : "Bipratip Dey",
		"year" : 2017,
		"picture" : "static/student_coordinators/biprateep.png"},
	{
		"name" : "Diptanil Roy",
		"year" : 2018,
		"picture" : "static/student_coordinators/debashish.jpg"},
	{
		"name" : "Pankaj Kumar",
		"year" : 2019,
		"picture" : "static/student_coordinators/pankaj.jpg"},
	{
		"name" : "Akshay Priyadarshi",
		"year" : 2021,
		"picture" : "static/student_coordinators/debashish.jpg"},
]

if not c.objects.all():
	for i in p:
		c(name=i["name"], year=i["year"], picture=i["picture"]).save()