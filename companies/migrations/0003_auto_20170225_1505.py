# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20170225_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AddField(
            model_name='stock',
            name='imgid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
