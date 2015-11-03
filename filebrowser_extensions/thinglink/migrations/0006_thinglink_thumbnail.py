# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('thinglink', '0005_auto_20150728_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='thinglink',
            name='thumbnail',
            field=filebrowser.fields.FileBrowseField(help_text='Upload thumbnail of your video / iframe / sliedshow', null=True, verbose_name='Thumbnail', max_length=255, blank=True),
        ),
    ]
