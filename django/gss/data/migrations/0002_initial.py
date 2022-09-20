# Generated by Django 4.1.1 on 2022-09-20 18:27

import datetime
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.linestring
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GpsLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('startts', models.DateTimeField(default=datetime.datetime.now)),
                ('endts', models.DateTimeField(default=datetime.datetime.now)),
                ('uploadts', models.DateTimeField(default=datetime.datetime.now)),
                ('the_geom', django.contrib.gis.db.models.fields.LineStringField(default=django.contrib.gis.geos.linestring.LineString(), srid=4326)),
                ('width', models.FloatField(default=3)),
                ('color', models.CharField(default='#FF0000', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('deviceid', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('previd', models.IntegerField(blank=True, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(), srid=4326)),
                ('altim', models.FloatField(default=-1)),
                ('ts', models.DateTimeField(default=datetime.datetime.now)),
                ('uploadts', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField(default='')),
                ('text', models.TextField(default='')),
                ('marker', models.CharField(default='circle', max_length=50)),
                ('size', models.FloatField(default=10)),
                ('rotation', models.FloatField(null=True)),
                ('color', models.CharField(default='#FF0000', max_length=9)),
                ('accuracy', models.FloatField(default=0)),
                ('heading', models.FloatField(default=0)),
                ('speed', models.FloatField(default=0)),
                ('speedaccuracy', models.FloatField(default=0)),
                ('form', models.JSONField(null=True)),
                ('projectid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.project')),
                ('surveyorid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.surveyor')),
            ],
        ),
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data', models.BinaryField(default=())),
                ('surveyorid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.surveyor')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(), srid=4326)),
                ('altim', models.FloatField(default=-1)),
                ('ts', models.DateTimeField(default=datetime.datetime.now)),
                ('uploadts', models.DateTimeField(default=datetime.datetime.now)),
                ('azimuth', models.FloatField(default=0)),
                ('text', models.TextField(default='')),
                ('thumbnail', models.BinaryField(default=())),
                ('imagedataid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.imagedata')),
                ('notesid', models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.note')),
                ('projectid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.project')),
                ('surveyorid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.surveyor')),
            ],
        ),
        migrations.CreateModel(
            name='GpsLogData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('the_geom', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(), dim=3, srid=4326)),
                ('ts', models.DateTimeField(default=datetime.datetime.now)),
                ('gpslogsid', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.gpslog')),
            ],
        ),
        migrations.AddField(
            model_name='gpslog',
            name='projectid',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.project'),
        ),
        migrations.AddField(
            model_name='gpslog',
            name='surveyorid',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='data.surveyor'),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['previd'], name='data_note_previd_61c531_idx'),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['ts'], name='data_note_ts_392f20_idx'),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['uploadts'], name='data_note_uploadt_434419_idx'),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['surveyorid'], name='data_note_surveyo_cd6ad3_idx'),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['projectid'], name='data_note_project_d67e9c_idx'),
        ),
        migrations.AddIndex(
            model_name='imagedata',
            index=models.Index(fields=['surveyorid'], name='data_imaged_surveyo_c0e769_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['ts'], name='data_image_ts_903f88_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['uploadts'], name='data_image_uploadt_201137_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['notesid'], name='data_image_notesid_561c6c_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['imagedataid'], name='data_image_imageda_91b21e_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['surveyorid'], name='data_image_surveyo_e3ac59_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['projectid'], name='data_image_project_692c2f_idx'),
        ),
        migrations.AddIndex(
            model_name='gpslogdata',
            index=models.Index(fields=['ts'], name='data_gpslog_ts_9a8770_idx'),
        ),
        migrations.AddIndex(
            model_name='gpslogdata',
            index=models.Index(fields=['gpslogsid'], name='data_gpslog_gpslogs_01a61e_idx'),
        ),
        migrations.AddIndex(
            model_name='gpslog',
            index=models.Index(fields=['uploadts'], name='data_gpslog_uploadt_69e6c8_idx'),
        ),
        migrations.AddIndex(
            model_name='gpslog',
            index=models.Index(fields=['surveyorid'], name='data_gpslog_surveyo_535fb4_idx'),
        ),
        migrations.AddIndex(
            model_name='gpslog',
            index=models.Index(fields=['projectid'], name='data_gpslog_project_39500b_idx'),
        ),
    ]
