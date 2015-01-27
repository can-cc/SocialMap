# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkPosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('picture', models.ImageField(upload_to=b'', blank=True)),
                ('postTime', models.DateTimeField(auto_now_add=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=32140)),
                ('postTpye', models.IntegerField(blank=True)),
                ('liveTime', models.IntegerField(blank=True)),
                ('user', models.ForeignKey(related_name='marks', to=settings.AUTH_USER_MODEL)),
                ('userInfo', models.ForeignKey(related_name='information', to='userManager.UserInformation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
