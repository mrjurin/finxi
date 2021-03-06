# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 01:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20170717_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='number_of_car_parks',
            field=models.IntegerField(verbose_name='Vagas'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='sell_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Venda'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Anunciante'),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
