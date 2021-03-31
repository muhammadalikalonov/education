from django.db import models
from django.shortcuts import reverse


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Country', blank=True)
    image = models.ImageField(upload_to='counrties/images', blank=True, verbose_name='Country Images')
    slug = models.SlugField(unique=True)
    banner = models.BooleanField(default=False, verbose_name='Banner')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страны'

class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name='Faculty_name', blank=True)
    study_year = models.CharField(max_length=100, blank=True, verbose_name='Study_year')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculty'


class Study_form(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название Форма обучения', blank=True)
    faculty =models.ManyToManyField(Faculty,related_name='facult', blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Форма обучения'
        verbose_name_plural = 'Форма обучения'




class Rating(models.Model):
    number = models.IntegerField(verbose_name='Rating',null=True, blank=True, default=0)


    def __str__(self):
        return str(self.number)


    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'





class University(models.Model):
    name = models.CharField(max_length=100, verbose_name='University Name', blank=True)
    university_city = models.CharField(max_length=100, verbose_name='University_city', blank=True)
    study_form  = models.ManyToManyField(Study_form  , related_name='studing', verbose_name="Форма обучения")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True, related_name='country')
    language = models.CharField('Language' , max_length=200 , null=True)
    year = models.CharField('Year founded' , max_length=200 , null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE , null =True, blank=True)
    faculty = models.ManyToManyField(Faculty, related_name='faculting',verbose_name='Faculty', blank=True)
    content = models.TextField(blank=True, verbose_name='Content')
    intake = models.CharField(max_length=100, verbose_name='All_Intake_months', blank=True)
    gallery1 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image1')
    image2 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image2')
    image3 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image3')
    image4 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image4')
    year_tuition_fee = models.CharField(max_length=100, verbose_name='Semester price', blank=True)
    on_campus_yearly = models.CharField(max_length=100, verbose_name='On_campus_yearly', blank=True)
    slug = models.SlugField(unique=True)
    top_universities = models.BooleanField(verbose_name='Top University', default=False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Университеты'
        verbose_name_plural = 'Университеты'


class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', blank=True)
    need = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документы для поступления'
        verbose_name_plural = 'Документы для поступления'
