# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 08:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0003_image_media_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_media_item',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image_media_item',
            name='width',
        ),
    ]