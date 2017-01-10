# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 04:49
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.TextField(unique=True)),
                ('html', models.TextField()),
                ('links', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('title', models.TextField()),
            ],
            options={
                'managed': True,
            },
        ),
    ]
