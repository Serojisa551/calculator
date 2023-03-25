from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path("main/testing/", views.members, name="testing"),
    path('main/testing/details/<slug:slug>', views.details, name='details'),
    path("main/testing/details/<int:id>", views.details, name="details"),
]
