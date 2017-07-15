# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20170715_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='rentPrice',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, verbose_name='Aluguel'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='sold_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Vendido em'),
        ),
    ]