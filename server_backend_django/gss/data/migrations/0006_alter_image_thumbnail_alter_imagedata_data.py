# Generated by Django 4.2.7 on 2023-11-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_image_thumbnail_alter_imagedata_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.BinaryField(default=()),
        ),
        migrations.AlterField(
            model_name='imagedata',
            name='data',
            field=models.BinaryField(default=()),
        ),
    ]