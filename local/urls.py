from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("login/", views.login, name = "login or signup"),
    path("upload/", views.upload, name = "UploadImage"),
    path("mark/", views.mark, name = "MarkAttendence"),
    path("check/", views.checkattendence, name = "CheckAttendence"),
    path("about/", views.about, name = "AboutUs"),
]