# Generated by Django 3.1.7 on 2021-03-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_phone1'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulting',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Added_date'),
        ),
        migrations.AddField(
            model_name='contact_form',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Added_date'),
        ),
    ]
