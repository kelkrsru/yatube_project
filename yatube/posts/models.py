from django.db import models
from django.contrib.auth import get_user_model


# Получаем пользователей
User = get_user_model()


class Post(models.Model):
    """Модель записи"""

    text = models.TextField(
        verbose_name='Текст записи',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        'Group',
        verbose_name='Группа записей',
        help_text='Привязка к конкретной группе записей',
        on_delete=models.CASCADE,
        related_name='groups',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return 'Запись #{pk} от {date}'.format(pk=self.pk, date=self.pub_date)


class Group(models.Model):
    """Модель группы для записей"""

    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Максимальная длина названия 200 символов.',
    )
    slug = models.SlugField(
        verbose_name='Адрес группы',
        help_text='Уникальный адрес группы, часть URL (например, для группы '
                  'любителей котиков slug будет равен cats: group/cats).',
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Текст, описывающий сообщество. Этот текст будет '
                  'отображаться на странице сообщества.'
    )

    class Meta:
        verbose_name = 'Группа для записей'
        verbose_name_plural = 'Группы для записей'

    def __str__(self):
        return self.title
