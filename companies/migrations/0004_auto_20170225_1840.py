# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20170225_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(blank=True, db_column='data')),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
