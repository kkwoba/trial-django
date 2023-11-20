from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html',{'link':'home'})


def about(request):
    context={'link':'about'}
    return render(request, "about.html", context)

def contact(request):
    return render(request, 'contact.html',{'navbar':'contact'})


def students(request):
    return render(request, 'students.html')


def add(request):
    return render(request,'add.html',{'navbar':'add'})

def viewdata(request):
    return render(request,'viewdata.html',{'navbar':'viewdata'})