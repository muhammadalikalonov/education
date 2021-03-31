from django.db import models


class Section_One(models.Model):
    image = models.ImageField(upload_to='section1/images', blank=True, verbose_name='Part_1 photo')
    content = models.TextField(blank=True, verbose_name='Content')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'







