# Generated by Django 3.2.9 on 2021-12-17 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_rename_sessionsmodel_sessionmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionmodel',
            name='invited_list',
        ),
    ]
