# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markPost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markposts',
            name='liveTime',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
