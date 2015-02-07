# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('markPost', '0005_auto_20150122_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markposts',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=True,
        ),
    ]
