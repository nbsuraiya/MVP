# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_auto_20171114_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
