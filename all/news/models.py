from django.db import models
from django.shortcuts import reverse


class News(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Новость', blank=True)
    image = models.ImageField(upload_to='counrties/images', blank=True, verbose_name='Для Фото')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    time = models.CharField(max_length=100,null =True, verbose_name='Время чтение')
    banner = models.BooleanField(default=True, verbose_name='Активные Новости')
    top_news = models.BooleanField(default=False, verbose_name='Топ новости')
    date = models.DateTimeField(auto_now_add=True , verbose_name='Дата добавления контента',null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '4.0 Новости'
        verbose_name_plural = '4.0 Новости'




