# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kynect', '0007_auto_20160615_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='marker',
            old_name='last_Location_Date',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='marker',
            old_name='last_Location_Latitude',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='marker',
            old_name='last_Location_Longitude',
            new_name='lng',
        ),
        migrations.AddField(
            model_name='device',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
