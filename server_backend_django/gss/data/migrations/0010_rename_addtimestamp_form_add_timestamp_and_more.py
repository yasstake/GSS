# Generated by Django 4.2.7 on 2023-11-15 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_form_addtimestamp_form_adduserinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='addtimestamp',
            new_name='add_timestamp',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='adduserinfo',
            new_name='add_userinfo',
        ),
    ]