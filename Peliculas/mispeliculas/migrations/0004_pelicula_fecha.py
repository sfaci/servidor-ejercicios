# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-19 16:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mispeliculas', '0003_auto_20180117_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha',
            field=models.DateField(default=datetime.date(2018, 1, 19)),
        ),
    ]
