# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('iframes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iframe',
            name='thumbnail',
            field=filebrowser.fields.FileBrowseField(help_text='Upload thumbnail of your video / iframe / sliedshow', null=True, verbose_name='Thumbnail', max_length=255, blank=True),
        ),
    ]
