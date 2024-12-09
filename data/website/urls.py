from django.contrib import admin
from website import views
from django.urls import path

urlpatterns = [
    path("home/",views.home),
    path("hello",views.hello),
  
]
