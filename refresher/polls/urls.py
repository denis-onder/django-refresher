from django.contrib import admin
from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("details/<int:question_id>/", views.details, name="details"),
]
