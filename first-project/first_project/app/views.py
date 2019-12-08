from django.http import HttpResponse
from django.shortcuts import render, reverse

from datetime import datetime
from os import getcwd, listdir


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    date = datetime.now()
    current_date = date.strftime('%Y-%m-%d')
    current_time = date.strftime('%H:%M:%S')
    msg = f'Сегодня {current_date}. ' \
          f'<br>Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    work_dir_path = getcwd()
    msg = f'Рабочая директория: {work_dir_path}<br><br>' \
          f'<i>Содержимое директории:</i><br>'
    work_dir_list = listdir(work_dir_path)
    for item in work_dir_list:
        file_string = f'– {item}<br>'
        msg += file_string
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    if not msg:
        raise NotImplemented
    return HttpResponse(msg)
