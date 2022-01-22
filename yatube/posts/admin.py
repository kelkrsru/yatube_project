from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """Класс для отображения моделей Post в админке"""

    # Отображаемые колонки
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    # Поля, которые можно редактировать на странице списка
    list_editable = ('group',)
    # Поля поиска
    search_fields = ('text',)
    # Поля фильтра
    list_filter = ('pub_date',)
    # Значение по умолчанию для пустого поля
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """Класс для отображения моделей Group в админке"""
    # Отображаемые колонки
    list_display = (
        'title',
        'description',
    )
    # Поля поиска
    search_fields = ('title',)


# Регистрируем модели в админке
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
