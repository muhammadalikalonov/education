# Generated by Django 3.1.7 on 2021-03-27 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_auto_20210327_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Rating')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Rating',
            },
        ),
        migrations.AddField(
            model_name='university',
            name='rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='university.rating'),
        ),
    ]
