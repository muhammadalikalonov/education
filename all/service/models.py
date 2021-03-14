from django.db import models


class Service_List(models.Model):
    image = models.ImageField(upload_to='service_list/images', blank=True, verbose_name='Service_list_image')
    content = models.TextField(blank=True, verbose_name='Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'





