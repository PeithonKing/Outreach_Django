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
		"picture" : "static/student_coordinators/debashish_jena.jpg"},
	{
		"name" : "Bipratip Dey",
		"year" : 2017,
		"picture" : "static/student_coordinators/bipratip_dey.png"},
	{
		"name" : "Diptanil Roy",
		"year" : 2018,
		"picture" : "static/student_coordinators/diptanil_roy.png"},
	{
		"name" : "Pankaj Kumar",
		"year" : 2019,
		"picture" : "static/student_coordinators/pankaj_kumar.jpg"},
	{
		"name" : "Akshay Priyadarshi",
		"year" : 2021,
		"picture" : "static/student_coordinators/akshay_priyadarshi.jpg"},
]

if not c.objects.all():
	print("Adding Student Coordinators!")
	for i in p:
		c(name=i["name"], year=i["year"], picture=i["picture"]).save()
		print(f"\tAdded {i['name']}.")
	print("Succesfully added all the Student Coordinators!\n\n")
else:
    print("There were things already in the database. So skipping...")