from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from mainApp import Service

menu = ['строка 1', 'строка 2']


def index(request):
    Service.createNewNotes('имя 1', 'содержание')
    posts = Note.objects.all()
    return render(request, 'mainApp/mainApp.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def categories(request, catid):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи<h1> <p>{catid}<p>")
