from django.db import models

class Specialist(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Имя Специалиста', blank=True)
    status = models.CharField(max_length=1000, verbose_name='Профессия Специалиста', blank=True)
    image = models.ImageField(upload_to='specialist/images', blank=True, verbose_name='Фото Специалиста')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '3.0 Специалист'
        verbose_name_plural = '3.0 Специалист'

class FAQ(models.Model):
    questions = models.CharField(max_length=1000, verbose_name='Вопросы', blank=True)
    answers = models.CharField(max_length=1000, verbose_name='Ответы', blank=True)

    def __str__(self):
        return f'{self.id}ый вопрос&ответ'

    class Meta:
        verbose_name = '3.1 Вопросы & Ответы'
        verbose_name_plural = '3.1 Вопросы & Ответы'


class Advantage(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название Преимущества', blank=True)
    image = models.ImageField(upload_to='advantage/images', blank=True, verbose_name='Фото Преимущества')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3.2 Преимущества'
        verbose_name_plural = '3.2 Преимущества'


class Testimonials(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Имя', blank=True)
    image = models.ImageField(upload_to='testimonials/images', blank=True, verbose_name='Фото для отзыва')
    content = models.TextField(blank=True, verbose_name='Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '3.3 Отзывы'
        verbose_name_plural = '3.3 Отзывы'


