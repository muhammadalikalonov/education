from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=1000, verbose_name='Phone', blank=True)
    phone1 = models.CharField(max_length=1000, verbose_name='Phone1', blank=True)
    telegram = models.CharField(max_length=1000, verbose_name='Telegram', blank=True)
    facebook = models.CharField(max_length=1000, verbose_name='Facebook', blank=True)
    instagram =models.CharField(max_length=1000, verbose_name='Instagram', blank=True)
    working_time = models.CharField(max_length=1000, verbose_name='Working_Time', blank=True)
    address = models.CharField(max_length=1000, blank=True, verbose_name='Address')
    address1 = models.CharField(max_length=1000, blank=True, verbose_name='Address')
    address2 = models.CharField(max_length=1000, blank=True, verbose_name='Address')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Contact_Form(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', blank=True)
    phone = models.CharField(max_length=100, default='+998', verbose_name='Phone', blank=True)
    content = models.CharField(max_length=100, verbose_name='Content', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Added_date', null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма для студентов'
        verbose_name_plural = 'Форма для студентов'




level = (('Начинающий (А1-А2)','Начинающий (А1-А2)'), ('Средний (В1-В2)','Средний (В1-В2)'),('Продвинутый(С1-С2)','Продвинутый(С1-С2)'))

study= (('Бакалавр','Бакалавр'),("Foundation","Foundation"),('Магистратура','Магистратура'))

class Consulting(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Name', blank=True)
    surname = models.CharField(max_length=1000, verbose_name='Surname', blank=True)
    birth_date = models.DateTimeField(verbose_name='Birth date', blank=True)
    city =models.CharField(max_length=1000, verbose_name='City', blank=True)
    phone = models.CharField(max_length=1000, verbose_name='Phone', blank=True)
    email = models.EmailField(blank=True, verbose_name='Email')
    english = models.CharField(max_length=1000,choices=level, blank=True, verbose_name='English level')
    study = models.CharField(max_length=1000,choices=study, blank=True, verbose_name='Study status')
    description = models.TextField(verbose_name='Info')
    take_date= models.DateTimeField(verbose_name='Taking date',blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Added_date' , null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'





