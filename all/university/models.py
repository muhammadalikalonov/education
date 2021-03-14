from django.db import models
from django.shortcuts import reverse


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Country', blank=True)
    image = models.ImageField(upload_to='counrties/images', blank=True, verbose_name='Country Images')
    slug = models.SlugField(unique=True)
    banner = models.BooleanField(default=False, verbose_name='Banner')
    quantity = models.CharField(max_length=100, verbose_name='Quantity')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страны'


class Bachelor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Faculty', blank=True)
    study_year = models.CharField(max_length=100, blank=True, verbose_name='Study_year')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Bachelor'
        verbose_name_plural = 'Bachelor'


class Masters(models.Model):
    name = models.CharField(max_length=100, verbose_name='Faculty', blank=True)
    study_year = models.CharField(max_length=100, blank=True, verbose_name='Study_year')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('single', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Masters'
        verbose_name_plural = 'Masters'





class University(models.Model):
    name = models.CharField(max_length=100, verbose_name='University Name', blank=True)
    university_city = models.CharField(max_length=100, verbose_name='University_city', blank=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True)
    star = models.PositiveIntegerField(verbose_name='Star', default='0')
    faculty_bachelor = models.ManyToManyField(Bachelor, related_name='faculty_name', verbose_name='Faculties bachelor', blank=True)
    masters_bachelor = models.ManyToManyField(Masters, related_name='faculty_name', verbose_name='Masters bachelor', blank=True)
    content = models.TextField(blank=True, verbose_name='Content')
    map = models.CharField(max_length=10000, blank=True, verbose_name='Map')
    intake = models.CharField(max_length=100, verbose_name='All_Intake_months', blank=True)
    intake_number = models.CharField(max_length=10, default=0, verbose_name='Intake_times')
    video_banner = models.CharField(max_length=1000, blank=True, verbose_name='Video_banner', default='IFRAME VIDEO')
    gallery1 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image1')
    image2 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image2')
    image3 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image3')
    image4 = models.ImageField(upload_to='university_images/images', blank=True, verbose_name='University_Image4')
    foundation = models.CharField(max_length=100, verbose_name='Foundation', blank=True)
    bachelor = models.CharField(max_length=100, verbose_name='Bachelor', blank=True)
    masters = models.CharField(max_length=100, verbose_name='Masters', blank=True)
    year_tuition_fee = models.CharField(max_length=100, verbose_name='Year_tuition_Fee', blank=True)
    on_campus_yearly = models.CharField(max_length=100, verbose_name='On_campus_yearly', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lists', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Университеты'
        verbose_name_plural = 'Университеты'



