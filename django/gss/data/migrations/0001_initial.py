# Generated by Django 4.0.4 on 2022-05-02 15:39

from django.db import migrations, models
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        CreateExtension('postgis'),
    ]
