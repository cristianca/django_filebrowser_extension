# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FBETestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('file_example', filebrowser_extensions.fields.FileBrowseField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TestExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('code', models.CharField(verbose_name='Code', unique=True, help_text='Copy paste link to iframe here', max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
