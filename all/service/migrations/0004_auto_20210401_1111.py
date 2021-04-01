# Generated by Django 3.1.7 on 2021-04-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20210329_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service_list',
            options={'verbose_name': '5.0 Услуги', 'verbose_name_plural': '5.0 Услуги'},
        ),
        migrations.AlterField(
            model_name='service_list',
            name='content',
            field=models.TextField(blank=True, verbose_name='Название Услуги'),
        ),
        migrations.AlterField(
            model_name='service_list',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Название Услуги'),
        ),
        migrations.AlterField(
            model_name='service_list',
            name='content_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Название Услуги'),
        ),
        migrations.AlterField(
            model_name='service_list',
            name='image',
            field=models.ImageField(blank=True, upload_to='service_list/images', verbose_name='Фото для услуг'),
        ),
    ]
