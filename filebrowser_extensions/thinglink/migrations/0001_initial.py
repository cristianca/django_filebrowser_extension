# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThingLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('code', models.CharField(verbose_name='Code', max_length=1000, help_text='Copy paste code from thinglink and paste here')),
            ],
            options={
                'verbose_name': 'ThingLink',
                'verbose_name_plural': 'ThingLinks',
            },
        ),
    ]
