# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=2)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
