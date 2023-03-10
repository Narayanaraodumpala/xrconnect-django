# Generated by Django 3.2.9 on 2021-12-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('media_id', models.CharField(max_length=128, unique=True)),
                ('media_type', models.CharField(max_length=128)),
                ('thumbnail_path', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=128)),
                ('upload_by', models.CharField(max_length=128)),
                ('access_type', models.CharField(max_length=128)),
                ('permitted_users', models.CharField(max_length=128)),
                ('path', models.CharField(max_length=128)),
                ('version', models.CharField(max_length=128)),
            ],
        ),
    ]
