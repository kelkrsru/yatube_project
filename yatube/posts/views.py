from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    template: str = 'posts/index.html'
    title = 'Главная страница'
    header = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'header': header,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template: str = 'posts/group_list.html'
    title = 'Страница записи'
    header = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'header': header,
    }
    return render(request, template, context)