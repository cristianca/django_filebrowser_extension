# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='code',
            field=models.CharField(verbose_name='Code', help_text='Copy paste link to iframe here', unique=True, max_length=1000),
        ),
    ]
