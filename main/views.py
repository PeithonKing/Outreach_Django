from django.http.response import HttpResponse
from django.shortcuts import render
from pathlib import Path

# import os

def images(p):
    path = Path(p)
    longPaths = list(path.glob("*.jpeg"))
    longPaths += list(path.glob("*.jpg"))
    longPaths += list(path.glob("*.png"))
    longPaths += list(path.glob("*.jfif"))
    paths = []
    for pa in longPaths:
        x = str(pa)[7:]
        paths.append([x, "s"+x])
    return paths





# Home Page, goes to "index.html"
def index(request):
    context = {"images": images("static/gallery/landing_page")}
    return render(request, "index.html", context)









# People
def people(request):
    return render(request, "people.html")









# Group of all pages under Open Day dropdown...
def open_day_about(request):
    return render(request, "open_day/about.html")

def open_day_2021(request):
    return render(request, "open_day/2021.html")

def open_day_past(request):
    return render(request, "open_day/past.html")

def open_day_gallery(request):
    context = {"p2017": images("static/gallery/open_day/2017"),
               "p2018": images("static/gallery/open_day/2018"),
               "p2019": images("static/gallery/open_day/2019"),
               "p2021": images("static/gallery/open_day/2021")}
    return render(request, "open_day/gallery.html", context)








# Group of all pages under Educational Visits dropdown...
def educational_visits_about(request):
    return render(request, "educational_visits/about.html")

def educational_visits_gallery(request):
    context = {"images": images("static/gallery/educational_visits")}
    return render(request, "educational_visits/gallery.html", context)









# Group of all pages under Vigyan Pratibha dropdown...
def vigyan_pratibha_about(request):
    return render(request, "vigyan_pratibha/about.html")

def vigyan_pratibha_resource_persons(request):
    return render(request, "vigyan_pratibha/resource_persons.html")

def vigyan_pratibha_gallery(request):
    context = {"Dec19": images("static/gallery/vigyan_pratibha/Dec19"),
               "Oct19": images("static/gallery/vigyan_pratibha/Oct19"),
               "Mar19": images("static/gallery/vigyan_pratibha/Mar19"),
               "ing18": images("static/gallery/vigyan_pratibha/inauguration18")}
    
    # print(f"\n\n{images('static/gallery/vigyan_pratibha/inauguration18')}\n\n")
    return render(request, "vigyan_pratibha/gallery.html", context)





# Webinars
def webinars(request):
    return render(request, "webinars.html")








# Contacts
def contacts(request):
    return render(request, "contacts.html")
