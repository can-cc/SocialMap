# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userTrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('footPoint', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('accuracy', models.FloatField(null=True, blank=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('stayLong', models.TimeField(null=True, blank=True)),
                ('user', models.ForeignKey(related_name='Track', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='UserFootprints',
        ),
    ]
