# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFootprints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('footPoint', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('accuracy', models.FloatField(null=True, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('stayLong', models.TimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
