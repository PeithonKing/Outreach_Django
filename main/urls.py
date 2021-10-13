from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
	# Home Page, goes to "index.html"
	path("", views.index, name='home'),


	# People
	path("people", views.people, name='people'),


	# Group of all pages under Open Day dropdown...
	path("open_day/about", views.open_day_about, name='open_day/about'),
	path("open_day/2021", views.open_day_2021, name='open_day/2021'),
	path("open_day/past", views.open_day_past, name='open_day/past'),
	path("open_day/gallery", views.open_day_gallery, name='open_day/gallery'),


	# Group of all pages under Educational Visits dropdown...
	path("educational_visits/about", views.educational_visits_about, name='educational_visits/about'),
	path("educational_visits/resources", views.educational_visits_resources, name='educational_visits/resources'),
	path("educational_visits/persons", views.educational_visits_persons, name='educational_visits/persons'),
	path("educational_visits/gallery", views.educational_visits_gallery, name='educational_visits/gallery'),


	# Group of all pages under Vigyan Pratibha dropdown...
	path("vigyan_pratibha/about", views.vigyan_pratibha_about, name='vigyan_pratibha/about'),
	path("vigyan_pratibha/resource_persons", views.vigyan_pratibha_resource_persons, name='vigyan_pratibha/resource_persons'),
	path("vigyan_pratibha/gallery", views.vigyan_pratibha_gallery, name='vigyan_pratibha/gallery'),


	# Webinars
	path("webinars", views.webinars, name='webinars'),


	# Contacts
	path("contacts", views.contacts, name='contacts'),
]