# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20161209_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crayfish',
            name='size',
            field=models.FloatField(default=0),
        ),
    ]