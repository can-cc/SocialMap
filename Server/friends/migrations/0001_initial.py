# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendsCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FriendsInUserCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAskFriends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stats', models.IntegerField()),
                ('askDate', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='askMF', to=settings.AUTH_USER_MODEL)),
                ('wtm', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
        migrations.CreateModel(
            name='UserFriends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IsHidden', models.BooleanField(default=False)),
                ('Friendliness', models.IntegerField(default=1)),
                ('DateCreated', models.DateField(auto_now_add=True)),
                ('friend', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='userFriend', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together=set([('user', 'follow')]),
        ),
    ]
