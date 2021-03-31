from django.db import models
from ..university.models import *



class Gallery(models.Model):
    image =models.ImageField(upload_to='students_gallery/images', blank=True, verbose_name='Gallery photo')

    def __str__(self):
        return f'{self.id} student '


    class Meta:
        verbose_name = 'Галерея Студентов'
        verbose_name_plural = 'Галерея Студентов'


class Students(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Name', blank=True)
    gallery = models.ForeignKey(Gallery , on_delete=models.CASCADE, verbose_name='Gallery', null=True)
    content = models.TextField(blank=True, verbose_name='Content')
    university = models.ForeignKey(University , on_delete=models.PROTECT , blank=True , verbose_name='University' )


    def __str__(self):
        return f'{self.id} student {self.name}'


    class Meta:
        verbose_name = 'Наши Студенты'
        verbose_name_plural = 'Наши Студенты'

