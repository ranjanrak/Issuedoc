# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdoc', '0015_auto_20171214_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
