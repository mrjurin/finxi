# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20170715_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='capital',
            field=models.BooleanField(default=False),
        ),
    ]