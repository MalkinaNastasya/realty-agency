# Generated by Django 3.1.4 on 2021-01-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0007_auto_20210112_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplomathesis',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/', verbose_name='Пояснительная записка'),
        ),
    ]
