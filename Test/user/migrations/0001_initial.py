# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-07 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientNumber', models.CharField(blank=True, max_length=6, null=True)),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
    ]