# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineFast', '0020_auto_20160510_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretor',
            name='foto',
            field=models.ImageField(null=True, upload_to='C:\\Program Files (x86)\\EasyPHP-Devserver-16.1\\eds-www'),
        ),
    ]
