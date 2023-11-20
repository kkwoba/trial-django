from django.urls import path

from . import views

app_name = "offline"

urlpatterns = [

    path('', views.home, name="home"),


]
