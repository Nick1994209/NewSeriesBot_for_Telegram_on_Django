# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20161028_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegrambot',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='telegrambot',
            name='username',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
