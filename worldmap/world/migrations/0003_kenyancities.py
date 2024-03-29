# Generated by Django 4.2.6 on 2023-10-15 12:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_worldcountries'),
    ]

    operations = [
        migrations.CreateModel(
            name='KenyanCities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('pop', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'KenyanCitiess',
            },
        ),
    ]
