# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineFast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]
