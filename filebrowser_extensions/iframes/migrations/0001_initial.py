# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('code', models.CharField(max_length=1000, unique=True, verbose_name='Code', help_text='Copy paste link to iframe here')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
