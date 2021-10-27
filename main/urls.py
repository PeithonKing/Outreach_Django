from django.contrib import admin
from django.urls import path
from main import views


admin.site.site_header = "Login to NISER Outreach"
admin.site.site_title = "NISER Outreach"
# admin.site.index_title = "NISER Outreach"
# admin.site.index_template = 


urlpatterns = [
	# Home Page, goes to "index.html"
	path("", views.index, name ='home'),


	# People
	path("people", views.people, name ='people'),


	# Group of all pages under Open Day dropdown...
	path("open_day/about", views.open_day_about, name ='open_day/about'),
	path("open_day/2021", views.open_day_2021, name ='open_day/2021'),
	path("open_day/past", views.open_day_past, name ='open_day/past'),
	path("open_day/student_coordinators", views.open_day_student_coordinators, name ='open_day/student_coordinators'),
	path("open_day/gallery", views.open_day_gallery, name ='open_day/gallery'),
	# path("open_day/feedback", views.open_day_feedback, name ='open_day/feedback'),


	# Group of all pages under Educational Visits dropdown...
	path("educational_visits/about", views.educational_visits_about, name ='educational_visits/about'),
	path("educational_visits/gallery", views.educational_visits_gallery, name ='educational_visits/gallery'),
	# path("educational_visits/feedback", views.educational_visits_feedback, name ='educational_visits/feedback'),


	# Group of all pages under Vigyan Pratibha dropdown...
	path("vigyan_pratibha/about", views.vigyan_pratibha_about, name ='vigyan_pratibha/about'),
	path("vigyan_pratibha/resource_persons", views.vigyan_pratibha_resource_persons, name ='vigyan_pratibha/resource_persons'),
	path("vigyan_pratibha/gallery", views.vigyan_pratibha_gallery, name ='vigyan_pratibha/gallery'),
	# path("vigyan_pratibha/feedback", views.vigyan_pratibha_feedback, name ='vigyan_pratibha/feedback'),


	# Webinars
	path("webinars", views.webinars, name ='webinars'),


	# Contacts
	path("contacts", views.contacts, name ='contacts')
]