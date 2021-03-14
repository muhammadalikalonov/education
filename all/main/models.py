from django.db import models


class FAQ(models.Model):
    questions = models.CharField(max_length=1000, verbose_name='Questions', blank=True)
    answers = models.CharField(max_length=1000, verbose_name='Answers', blank=True)

    def __str__(self):
        return self.questions

    class Meta:
        verbose_name = 'Вопросы & Ответы'
        verbose_name_plural = 'Вопросы & Ответы'


class Advantage(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Advantage', blank=True)
    image = models.ImageField(upload_to='advantage/images', blank=True, verbose_name='Advantage image')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'


class Testimonials(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Name', blank=True)
    image = models.ImageField(upload_to='testimonials/images', blank=True, verbose_name='Slider photo')
    content = models.TextField(blank=True, verbose_name='Content')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


