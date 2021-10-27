# from typing_extensions import Required
from django.db import models
from django.utils import timezone as dt
from ckeditor.fields import RichTextField

# class CommentOpenDay(models.Model):
#     name = models.CharField("Name", max_length=50)
#     email = models.EmailField("Email Address")
#     comment = models.TextField(default = "")
#     time = models.DateTimeField(default=None)
#     show = models.BooleanField(default=False)
 
#     def __str__(self):
#         if self.show:
#             return "[shown]" + " " + self.comment
#         else:
#             return "[NOT shown]" + " " + self.comment

# class CommentEducationalVisits(models.Model):
#     name = models.CharField("Name", max_length=50)
#     email = models.EmailField("Email Address")
#     comment = models.TextField(default = "")
#     time = models.DateTimeField(default=None)
#     show = models.BooleanField(default=False)

#     def __str__(self):
#         if self.show:
#             return "[shown]" + " " + self.comment
#         else:
#             return "[NOT shown]" + " " + self.comment
    
# class CommentVigyanPratibha(models.Model):
#     name = models.CharField("Name", max_length=50)
#     email = models.EmailField("Email Address")
#     comment = models.TextField(default = "")
#     time = models.DateTimeField(default=None)
#     show = models.BooleanField(default=False)

#     def __str__(self):
#         if self.show:
#             return "[shown]" + " " + self.comment
#         else:
#             return "[NOT shown]" + " " + self.comment


class News(models.Model):
    news = models.TextField(blank=True)
    URL = models.URLField(default="", blank=True)
    new = models.BooleanField(default=False)
    
    def __str__(self):
        if self.new:
            return "[new]" + " " + self.news
        else:
            return "[old]" + " " + self.news


class Coordinators(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default = 2022)
    picture = models.ImageField(upload_to = "static/student_coordinators")
    
    def __str__(self):
        return f"[{self.year}] {self.name}"


class Webinars(models.Model):
    name = models.TextField(verbose_name="Name of the Webinar", null=True)
    time = models.DateTimeField(default=None)
    poster = models.ImageField(default="static/no-poster-available.jpg", upload_to = "static/webinars", verbose_name="Posters (if Any) Image files only")
    info = RichTextField(verbose_name="Informations (All other things you want to write)", null=True)
    
    def __str__(self):
        if self.time > dt.now():
            return f"[upcoming], Date: {self.time}, {self.name}"
        else:
            return f"[past], Date: {self.time}, {self.name}"
