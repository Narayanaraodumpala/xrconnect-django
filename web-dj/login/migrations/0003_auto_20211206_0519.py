# Generated by Django 3.2.9 on 2021-12-06 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20211202_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionmodel',
            name='date_modified',
            field=models.CharField(default=datetime.date(2021, 12, 6), max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionmodel',
            name='end_date',
            field=models.CharField(default=datetime.date(2021, 12, 6), max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionmodel',
            name='start_date',
            field=models.CharField(default=datetime.date(2021, 12, 6), max_length=50),
        ),
    ]
