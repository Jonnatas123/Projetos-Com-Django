# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-08 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineFast', '0009_diretor_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diretor',
            name='caminho_foto',
        ),
        migrations.AlterField(
            model_name='diretor',
            name='file',
            field=models.FileField(null=True, upload_to='C:\\projetosDjango\\mysite\\imagens'),
        ),
    ]
