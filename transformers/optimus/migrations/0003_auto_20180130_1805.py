# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('optimus', '0002_restaurantlocation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]