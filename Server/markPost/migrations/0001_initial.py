# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings
import markPost.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarkPosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('picture', models.ImageField(null=True, upload_to=markPost.models.Pcontent_file_name, blank=True)),
                ('postTime', models.DateTimeField(auto_now_add=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('accuracy', models.FloatField(null=True, blank=True)),
                ('postTpye', models.IntegerField(null=True, blank=True)),
                ('liveTime', models.IntegerField(null=True, blank=True)),
                ('valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(related_name='marks', to=settings.AUTH_USER_MODEL)),
                ('userInfo', models.ForeignKey(related_name='information', to='userManager.UserInformation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='markPosts',
            field=models.ForeignKey(related_name='comment', to='markPost.MarkPosts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(related_name='review', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
