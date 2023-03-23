from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("testing/", views.members, name="testing"),
    path('testing/details/<slug:slug>', views.details, name='details'),
    path("testing/details/<int:id>", views.details, name="details"),
]
