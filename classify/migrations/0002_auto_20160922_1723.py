# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='id',
        ),
        migrations.AlterField(
            model_name='publication',
            name='pmid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
