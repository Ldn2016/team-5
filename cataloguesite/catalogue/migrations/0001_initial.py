# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=1000)),
                ('other_data', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='quantity',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Store'),
        ),
    ]
