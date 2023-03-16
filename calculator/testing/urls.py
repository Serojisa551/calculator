from django.urls import path
from . import views

urlpatterns = [
    path("testing/", views.members, name="testing"),
    path("testing/details/<int:id>", views.details, name="details"),
]
