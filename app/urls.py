# File: urls.py
from django.contrib import admin
from django.urls import path
from . import views

app_name = "app"  # this is used for Namespacing URL names if there are more than one apps in the project
urlpatterns = [
    path('', views.task_list, name='task_list'), # Name the url to be used in the tamplates
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]