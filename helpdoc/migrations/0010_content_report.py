# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0009_auto_20171203_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='report',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
