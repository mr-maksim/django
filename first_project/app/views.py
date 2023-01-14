from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os 


def home_view(request):
    template_name = 'app/home.html'
   
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse("time"),
        'Показать содержимое рабочей директории': reverse("workdir")
    }
    

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    work_dir_list= os.listdir()
    msg = []
    for item in work_dir_list:
        msg.append(f'{item}, ')
    return HttpResponse(msg)
