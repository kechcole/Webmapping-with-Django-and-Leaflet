# Generated by Django 4.2.6 on 2023-10-14 19:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldCountries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fips', models.CharField(max_length=2, null=True)),
                ('iso2', models.CharField(max_length=2)),
                ('iso3', models.CharField(max_length=3)),
                ('un', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('area', models.IntegerField()),
                ('pop2005', models.BigIntegerField()),
                ('region', models.IntegerField()),
                ('subregion', models.IntegerField()),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'WorldCountries',
            },
        ),
    ]
