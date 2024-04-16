from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createEntry", views.createEntry, name="createEntry"),
    path("<str:title>",views.getEntry,name="title")
]

