# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0004_publication_fulltextviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='toolname',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
