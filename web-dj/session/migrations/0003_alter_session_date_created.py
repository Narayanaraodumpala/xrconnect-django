# Generated by Django 3.2.9 on 2022-01-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0002_auto_20220106_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
