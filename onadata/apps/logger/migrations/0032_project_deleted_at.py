# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-20 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0031_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]