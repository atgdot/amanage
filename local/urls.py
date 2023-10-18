from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("Home", views.Home, name = "Home"),
    path("signin", views.signin, name = "signin"),
    path("signup", views.signup, name = "signup"),
    path("mark", views.mark, name = "MarkAttendence"),
    path("check", views.checkattendence, name = "CheckAttendence"),
    path("about", views.about, name = "AboutUs"),
    path("capture_image", views.capture_image_view, name= "capture_image"),
]