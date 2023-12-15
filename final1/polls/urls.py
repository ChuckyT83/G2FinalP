from django.urls import path
from django.contrib import admin
from . import views


app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("compare/", views.compare, name="compare"),
    path("survey/", views.survey, name="survey"),
    path("tryagain/", views.tryAgain, name="tryAgain"),        
    path("register/", views.register, name="register"),
    path("logout/", views.logoutRequest, name="logout"),
]