# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineFast', '0005_auto_20160323_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='em_cartaz',
            field=models.BooleanField(default=True, verbose_name='Em Cartaz'),
        ),
    ]
