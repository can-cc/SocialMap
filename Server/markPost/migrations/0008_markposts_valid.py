# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markPost', '0007_auto_20150207_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='markposts',
            name='valid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
