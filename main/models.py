# from typing_extensions import Required
from django.db import models
# from django.utils import timezone as dt
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


# class Webinars(models.Model):
    
#     body = RichTextField(blank = True, null = True)
    
#     def __str__(self):
#         if self.new:
#             return "[new]" + " " + self.news
#         else:
#             return "[old]" + " " + self.news
