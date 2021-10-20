from django.http.response import HttpResponse
from django.shortcuts import render
from pathlib import Path
from .models import *
from .forms import *
from django.utils import timezone as dt

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
    return render(request, "index.html", 
        {"images": images("static/gallery/landing_page"),
        "allNews": News.objects.all()
        })








# People
def people(request):
    return render(request, "people.html", {"allNews": News.objects.all()})









# Group of all pages under Open Day dropdown...
def open_day_about(request):
    return render(request, "open_day/about.html", {"allNews": News.objects.all()})

def open_day_2021(request):
    return render(request, "open_day/2021.html", {"allNews": News.objects.all()})

def open_day_past(request):
    return render(request, "open_day/past.html", {"allNews": News.objects.all()})

def open_day_gallery(request):
    context = {"p2017": images("static/gallery/open_day/2017"),
               "p2018": images("static/gallery/open_day/2018"),
               "p2019": images("static/gallery/open_day/2019"),
               "p2021": images("static/gallery/open_day/2021"),
               "allNews": News.objects.all()}
    return render(request, "open_day/gallery.html", context)

# def open_day_feedback(request):
#     submitted = False
#     if request.method == "POST":
#         form = OpenDayForm(request.POST)
#         if form.is_valid():
#             if request.POST['comment'] == "":
#                 pass
#             else:
#                 temp = form.save(commit=False)
#                 temp.time = dt.now()
#                 temp.save()
#                 submitted = True
#         else: print("\n\n\n\nInvalid Form\n\n\n\n")
#     else:
#         form = OpenDayForm
#     return render(request, "open_day/feedback.html",
#         {"form": form,
#         "submitted": submitted,
#         "comments": CommentOpenDay.objects.all().order_by("-time"),
#         "allNews": News.objects.all()
#         })










# Group of all pages under Educational Visits dropdown...
def educational_visits_about(request):
    return render(request, "educational_visits/about.html", {"allNews": News.objects.all()})

def educational_visits_gallery(request):
    context = {"images": images("static/gallery/educational_visits"), "allNews": News.objects.all()}
    return render(request, "educational_visits/gallery.html", context)

# def educational_visits_feedback(request):
#     submitted = False
#     if request.method == "POST":
#         form = EducationalVisitsForm(request.POST)
#         if form.is_valid():
#             if request.POST['comment'] == "":
#                 pass
#             else:
#                 temp = form.save(commit=False)
#                 temp.time = dt.now()
#                 temp.save()
#                 submitted = True
#         else: print("\n\n\n\nInvalid Form\n\n\n\n")
#     else:
#         form = EducationalVisitsForm
#     return render(request, "educational_visits/feedback.html",
#         {"form": form,
#         "submitted": submitted,
#         "comments": CommentEducationalVisits.objects.all().order_by("-time"),
#         "allNews": News.objects.all()
#         })











# Group of all pages under Vigyan Pratibha dropdown...
def vigyan_pratibha_about(request):
    return render(request, "vigyan_pratibha/about.html", {"allNews": News.objects.all()})

def vigyan_pratibha_resource_persons(request):
    return render(request, "vigyan_pratibha/resource_persons.html", {"allNews": News.objects.all()})

def vigyan_pratibha_gallery(request):
    context = {"Dec19": images("static/gallery/vigyan_pratibha/Dec19"),
               "Oct19": images("static/gallery/vigyan_pratibha/Oct19"),
               "Mar19": images("static/gallery/vigyan_pratibha/Mar19"),
               "ing18": images("static/gallery/vigyan_pratibha/inauguration18"),
               "allNews": News.objects.all()}
    return render(request, "vigyan_pratibha/gallery.html", context)

# def vigyan_pratibha_feedback(request):
#     submitted = False
#     if request.method == "POST":
#         # print(f"\n\n{request.POST['comment']}\n\n")
#         # if request.POST['comment'] == "":
#         #     print("Congrats!!\n\n")
#         form = VigyanPratibhaForm(request.POST)
#         if form.is_valid():
#             if request.POST['comment'] == "":
#                 pass
#             else:
#                 temp = form.save(commit=False)
#                 temp.time = dt.now()
#                 temp.save()
#                 submitted = True
#         else: print("\n\n\n\nInvalid Form\n\n\n\n")
#     else:
#         form = VigyanPratibhaForm
#     return render(request, "vigyan_pratibha/feedback.html",
#         {"form": form,
#         "submitted": submitted,
#         "comments": CommentVigyanPratibha.objects.all().order_by("-time"),
#         "allNews": News.objects.all()
#         })









# Webinars
def webinars(request):
    return render(request, "webinars.html", {"allNews": News.objects.all()})








# Contacts
def contacts(request):
    return render(request, "contacts.html", {"allNews": News.objects.all()})
