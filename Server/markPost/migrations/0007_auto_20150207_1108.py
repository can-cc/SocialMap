# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markPost.models


class Migration(migrations.Migration):

    dependencies = [
        ('markPost', '0006_auto_20150205_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markposts',
            name='picture',
            field=models.ImageField(null=True, upload_to=markPost.models.content_file_name, blank=True),
            preserve_default=True,
        ),
    ]
