# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_remove_workpage_marketing_only'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workpage',
            name='intro',
        ),
    ]