# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
