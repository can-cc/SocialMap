# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markPost', '0002_auto_20150121_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='markposts',
            name='accuracy',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
