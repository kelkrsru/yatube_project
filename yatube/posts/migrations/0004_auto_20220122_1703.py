# Generated by Django 2.2.19 on 2022-01-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220122_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(help_text='Уникальный адрес группы, часть URL (например, для группы любителей котиков slug будет равен cats: group/cats).', verbose_name='Адрес группы'),
        ),
    ]