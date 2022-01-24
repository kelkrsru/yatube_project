from typing import Dict, Any
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


POSTS_PER_PAGE = 10


def index(request):
    """View-функция для главной страницы"""

    # Переменные функции
    template: str = 'posts/index.html'
    title: str = 'Последние обновления на сайте'
    header: str = 'Это главная страница проекта Yatube'
    # Получаем из БД 10 последних записей
    posts: Post = Post.objects.all()[:POSTS_PER_PAGE]
    # Формируем словарь context
    context: Dict[str, Any] = {
        'title': title,
        'header': header,
        'posts': posts,
    }
    # Рендерим страницу
    return render(request, template, context)


def group_posts(request, slug):
    """View-функция для страницы группы записей"""

    # Переменные функции
    template: str = 'posts/group_list.html'
    title: str = 'Записи сообщества'
    # Получаем из БД группу для записи
    group: Group = get_object_or_404(Group, slug=slug)
    # Получаем из БД 10 последних записей для группы
    posts: Post = group.group_posts.all()[:POSTS_PER_PAGE]
    # Формируем словарь context
    context: Dict[str, Any] = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    # Рендерим страницу
    return render(request, template, context)
