# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0002_useraskfriends'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follower', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='userFollowers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFollows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('follow', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='userFollows', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
