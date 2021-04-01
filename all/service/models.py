from django.db import models


class Service_List(models.Model):
    image = models.ImageField(upload_to='service_list/images', blank=True, verbose_name='Фото для услуг')
    content = models.TextField(blank=True, verbose_name='Название Услуги')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '5.0 Услуги'
        verbose_name_plural = '5.0 Услуги'





