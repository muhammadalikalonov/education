from django.db import models
from django.shortcuts import reverse


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Страна', blank=True)
    image = models.ImageField(upload_to='counrties/images', blank=True, verbose_name='Фото страны')
    slug = models.SlugField(unique=True)
    banner = models.BooleanField(default=False, verbose_name='Топ страны')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '7.0 Страны'
        verbose_name_plural = '7.0 Страны'
        ordering = ['-id']


class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', blank=True)
    study_year = models.CharField(max_length=100, blank=True, verbose_name='Период учебы')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = '7.1 Факультет'
        verbose_name_plural = '7.1 Факультет'
        ordering = ['-id']


class Study_form(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название Форма обучения', blank=True)
    faculty = models.ManyToManyField(Faculty, related_name='facult', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '7.2 Форма обучения'
        verbose_name_plural = '7.2 Форма обучения'
        ordering = ['-id']


class Rating(models.Model):
    number = models.IntegerField(verbose_name='Рейтинг для университета', null=True, blank=True, default=0)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = '7.3 Рейтинг'
        verbose_name_plural = '7.3 Рейтинг'
        ordering = ['-id']


cur = (('$', '$'), ("£", "£"), ('€', '€'), ('₽', '₽'))


class University(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', blank=True)
    university_city = models.CharField(max_length=100, verbose_name='Город', blank=True)

    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, related_name='country')
    language = models.CharField('Язык обучения', max_length=200, null=True)
    year = models.CharField('Университет основан', max_length=200, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(blank=True, verbose_name='Описание')
    intake = models.CharField(max_length=100, verbose_name='Месяцы приема', blank=True)
    gallery1 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image1')
    image2 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image2')
    image3 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image3')
    image4 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image4')
    year_tuition_fee = models.PositiveBigIntegerField(verbose_name='Цена/год', blank=True, null=True)
    on_campus_yearly = models.PositiveBigIntegerField(verbose_name='Цена/проживание', blank=True, null=True)
    slug = models.SlugField(unique=True)
    currency = models.CharField('Валюта', choices=cur, max_length=200, null=True)
    top_universities = models.BooleanField(verbose_name='Top Университет', default=False)
    logo = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_LOGO')
    study_form = models.ManyToManyField(Study_form, related_name='studing', verbose_name="Форма обучения")
    faculty = models.ManyToManyField(Faculty, related_name='faculting',
                                     verbose_name='Факультет(выберите основные 4-5 факультета)', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '7.4 Университеты'
        verbose_name_plural = '7.4 Университеты'
        ordering = ['-id']


class Faculty_for_Forms(models.Model):
    study_faculty_form = models.ForeignKey(Study_form, blank=True, on_delete=models.CASCADE, null=True, default=None)
    content = models.ForeignKey(University, blank=True, on_delete=models.CASCADE,
                                related_name='%(class)s_requests_created', null=True, default=None)
    faculty_form = models.ManyToManyField(Faculty, related_name='faculty_f',
                                          verbose_name='Факультет(выберите основные 4-5 факультета)', blank=True)

    def __str__(self):
        return self.study_faculty_form.name

    class Meta:
        verbose_name = '7.4.1 Faculty_Forms'
        verbose_name_plural = '7.4.1 Faculty_Forms'


class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name='Документ', blank=True)
    need = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '7.5 Документы для поступления'
        verbose_name_plural = '7.5 Документы для поступления'
        ordering = ['-id']
