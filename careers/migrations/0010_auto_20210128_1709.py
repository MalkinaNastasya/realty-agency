# Generated by Django 3.1.5 on 2021-01-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0009_auto_20210128_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencyrealtors',
            name='year_of_foundation',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Год основания'),
        ),
    ]