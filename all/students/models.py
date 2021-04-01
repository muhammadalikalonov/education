from django.db import models
from ..university.models import *



class Gallery(models.Model):
    image =models.ImageField(upload_to='students_gallery/images', blank=True, verbose_name='Фото галерея студентов')

    def __str__(self):
        return f'{self.id} фото студента'


    class Meta:
        verbose_name = '6.0 Галерея Студентов'
        verbose_name_plural = '6.0 Галерея Студентов'


class Students(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Имя', blank=True)
    gallery = models.ManyToManyField(Gallery , related_name='gal')
    content = models.TextField(blank=True, verbose_name='Описание')
    university = models.ForeignKey(University , on_delete=models.PROTECT , blank=True , verbose_name='Университет')
    date = models.DateTimeField(verbose_name='Дата поступления',null=True)

    def __str__(self):
        return f'{self.id} student {self.name}'


    class Meta:
        verbose_name = '6.1 Наши Студенты'
        verbose_name_plural = '6.1 Наши Студенты'

