from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=1000, verbose_name='Тел.номер', blank=True)
    phone1 = models.CharField(max_length=1000, verbose_name='Доп.Тел.номер', blank=True)
    telegram = models.CharField(max_length=1000, verbose_name='Telegram', blank=True)
    facebook = models.CharField(max_length=1000, verbose_name='Facebook', blank=True)
    instagram =models.CharField(max_length=1000, verbose_name='Instagram', blank=True)
    youtube =models.CharField(max_length=1000, verbose_name='Youtube', blank=True)
    working_time = models.CharField(max_length=1000, verbose_name='Время работы', blank=True)
    address = models.CharField(max_length=1000, blank=True, verbose_name='Адрес')
    address1 = models.CharField(max_length=1000, blank=True, verbose_name='Адрес1')
    address2 = models.CharField(max_length=1000, blank=True, verbose_name='Адрес2')

    def __str__(self):
        return f'Контактые данные'

    class Meta:
        verbose_name = '2.1 Контакты'
        verbose_name_plural = '2.1 Контакты'


class Contact_Form(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True)
    phone = models.CharField(max_length=100, default='+998', verbose_name='Тел.номер', blank=True)
    content = models.CharField(max_length=100, verbose_name='Доп.инфо', blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Оформлена заявка', null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '2.2 Форма для студентов'
        verbose_name_plural = '2.2 Форма для студентов'




level = (('Начинающий (А1-А2)','Начинающий (А1-А2)'), ('Средний (В1-В2)','Средний (В1-В2)'),('Продвинутый(С1-С2)','Продвинутый(С1-С2)'))

study= (('Бакалавр','Бакалавр'),("Foundation","Foundation"),('Магистратура','Магистратура'))

class Consulting(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=1000, verbose_name='Фамилия', blank=True)
    birth_date = models.DateTimeField(verbose_name='Дата рождения', blank=True)
    city =models.CharField(max_length=1000, verbose_name='Город', blank=True)
    phone = models.CharField(max_length=1000, verbose_name='Тел.номер', blank=True)
    email = models.EmailField(blank=True, verbose_name='Email')
    english = models.CharField(max_length=1000,choices=level, blank=True, verbose_name='Уровень анг.яз')
    study = models.CharField(max_length=1000,choices=study, blank=True, verbose_name='Направления')
    description = models.TextField(verbose_name='Инфо о себе')
    take_date= models.DateTimeField(verbose_name='Дата сдачи',blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Форма оформлена' , null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '2.0 Заявка на рус'
        verbose_name_plural = '2.0 Заявка на рус'



level_up = (('Boshlang`ich (А1-А2)', 'Boshlang`ich (А1-А2)'), ('O`rtacha (В1-В2)', 'O`rtacha (В1-В2)'),
         ('Mukammal (С1-С2)', 'Mukammal (С1-С2)'))

study_up = (('Bakalavr', 'Bakalavr'), ("Foundation", "Foundation"), ('Magistratura', 'Magistratura'))

class Consulting_uz(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=1000, verbose_name='Фамилия', blank=True)
    birth_date = models.DateTimeField(verbose_name='Дата рождения', blank=True)
    city =models.CharField(max_length=1000, verbose_name='Город', blank=True)
    phone = models.CharField(max_length=1000, verbose_name='Тел.номер', blank=True)
    email = models.EmailField(blank=True, verbose_name='Email')
    english = models.CharField(max_length=1000,choices=level_up, blank=True, verbose_name='Уровень анг.яз')
    study = models.CharField(max_length=1000,choices=study_up, blank=True, verbose_name='Направления')
    description = models.TextField(verbose_name='Инфо о себе')
    take_date= models.DateTimeField(verbose_name='Дата сдачи',blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Форма оформлена' , null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '3.0 Заявка на узб'
        verbose_name_plural = '3.0 Заявка на узб'


