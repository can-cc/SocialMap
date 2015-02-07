# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userManager.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0004_auto_20150205_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='portrait',
            field=models.ImageField(default=b'user/portrait/default.jpeg', null=True, upload_to=userManager.models.content_file_name, blank=True),
            preserve_default=True,
        ),
    ]
