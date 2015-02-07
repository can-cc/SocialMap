# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userManager.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0003_delete_userfootprints'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='sex',
            field=models.IntegerField(default=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='portrait',
            field=models.ImageField(default=b'user/portrait/default', null=True, upload_to=userManager.models.content_file_name, blank=True),
            preserve_default=True,
        ),
    ]
