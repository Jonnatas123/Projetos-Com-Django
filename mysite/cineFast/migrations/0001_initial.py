# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('descricao', models.TextField()),
                ('data_lancamento', models.DateField(verbose_name='Data de Lançamento')),
                ('caminho_imagem', models.CharField(max_length=100)),
            ],
        ),
    ]
