# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markPost', '0004_auto_20150122_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markposts',
            name='postTpye',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
