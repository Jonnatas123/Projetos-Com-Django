# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineFast', '0017_auto_20160508_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretor',
            name='foto',
            field=models.ImageField(null=True, upload_to='imagens\\diretores'),
        ),
    ]
