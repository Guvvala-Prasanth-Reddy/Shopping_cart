# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-10 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='Rating',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
