# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0012_auto_20171127_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='mysite/donations/static/donations/images/'),
        ),
    ]
