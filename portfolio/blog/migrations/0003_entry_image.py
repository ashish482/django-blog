# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170331_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='No image', upload_to='media'),
        ),
    ]
