# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kynect', '0003_auto_20170719_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='verified',
            new_name='is_verified',
        ),
    ]
