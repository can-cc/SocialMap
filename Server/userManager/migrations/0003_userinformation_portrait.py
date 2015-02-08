# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userManager.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0002_remove_userinformation_portrait'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='portrait',
            field=models.ImageField(default=b'user/portrait/default.jpeg', null=True, upload_to=userManager.models.content_file_name2, blank=True),
            preserve_default=True,
        ),
    ]
