# Generated by Django 3.1.7 on 2021-03-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210325_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='section_one',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='section_one',
            name='content_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Content'),
        ),
    ]
