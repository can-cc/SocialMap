# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0002_auto_20150122_0132'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFootprints',
        ),
    ]
