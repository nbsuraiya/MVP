# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0011_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='../static/donations/images/'),
        ),
    ]
