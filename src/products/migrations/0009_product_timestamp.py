# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 23:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180206_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 2, 7, 23, 28, 29, 419525, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
