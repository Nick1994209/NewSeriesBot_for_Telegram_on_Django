# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161028_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegrambot',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telegrambot',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
