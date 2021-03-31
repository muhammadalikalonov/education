from django.db import models
from django.shortcuts import reverse


class News(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Title', blank=True)
    image = models.ImageField(upload_to='counrties/images', blank=True, verbose_name='Country Images')
    slug = models.SlugField(unique=True)
    banner = models.BooleanField(default=False, verbose_name='Valid news')
    description = models.TextField(verbose_name='Description')
    top_news =models.BooleanField(default=False, verbose_name='Top_news')
    time =models.CharField(max_length=100,null =True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'




