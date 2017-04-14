# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=255)),
                ('thumbnail', filebrowser.fields.FileBrowseField(help_text='Upload thumbnail of your video / iframe / sliedshow', verbose_name='Thumbnail', null=True, max_length=255, blank=True)),
                ('code', models.TextField(help_text='Copy paste link to iframe here', verbose_name='Code', max_length=1000)),
            ],
            options={
                'verbose_name': 'Youtube',
                'verbose_name_plural': 'Youtubes',
            },
        ),
    ]
