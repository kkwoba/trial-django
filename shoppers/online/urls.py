
from django.urls import path

from .import views
from django.conf.urls.static import static
from django.conf import settings

APP_NAME= "online"

urlpatterns = [

    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('add/', views.add, name="add"),
    path('viewdata',views.viewdata, name="viewdta")


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)