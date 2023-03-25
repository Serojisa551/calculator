from django.urls import path
from . import views

urlpatterns = [
    path('main/user/', views.members, name='user'),
]