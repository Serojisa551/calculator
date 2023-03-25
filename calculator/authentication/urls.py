from django.urls import path
from .views import authentication
from . import views

urlpatterns = [
    path("", authentication, name="authentication"),
    path("register/", views.register, name="register"),
]
