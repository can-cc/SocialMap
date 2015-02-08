# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import userManager.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'default', max_length=50, blank=True)),
                ('interesting', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickName', models.CharField(unique=True, max_length=20)),
                ('sex', models.IntegerField(default=3)),
                ('portrait', models.ImageField(default=b'user/portrait/default.jpeg', null=True, upload_to=userManager.models.content_file_name2, blank=True)),
                ('personalDescription', models.TextField(null=True, blank=True)),
                ('phoneNumber', models.BigIntegerField(null=True, blank=True)),
                ('country', models.IntegerField(null=True, blank=True)),
                ('province', models.IntegerField(null=True, blank=True)),
                ('city', models.IntegerField(null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('school', models.CharField(max_length=50, null=True, blank=True)),
                ('schoolId', models.IntegerField(null=True, blank=True)),
                ('cardId', models.BigIntegerField(null=True, blank=True)),
                ('nowCity', models.IntegerField(null=True, blank=True)),
                ('publicMail', models.EmailField(max_length=75, null=True, blank=True)),
                ('publicPhoneNumber', models.BigIntegerField(null=True, blank=True)),
                ('QQ', models.BigIntegerField(null=True, blank=True)),
                ('lastIp', models.IPAddressField(null=True, blank=True)),
                ('lastActivity', models.TimeField(null=True, blank=True)),
                ('userType', models.IntegerField(null=True, blank=True)),
                ('loginTimes', models.IntegerField(default=1)),
                ('hitTimes', models.IntegerField(default=0)),
                ('activityScore', models.IntegerField(default=0)),
                ('friendCount', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInformationDisplay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personalDescription', models.TextField(blank=True)),
                ('phoneNumber', models.BooleanField(default=True)),
                ('country', models.BooleanField(default=True)),
                ('province', models.BooleanField(default=True)),
                ('city', models.BooleanField(default=True)),
                ('birthday', models.BooleanField(default=True)),
                ('school', models.BooleanField(default=True)),
                ('schoolId', models.BooleanField(default=True)),
                ('interest', models.BooleanField(default=True)),
                ('cardId', models.BooleanField(default=False)),
                ('nowCity', models.BooleanField(default=True)),
                ('publicMail', models.BooleanField(default=True)),
                ('publicPhoneNumber', models.BooleanField(default=True)),
                ('QQ', models.BooleanField(default=True)),
                ('userType', models.BooleanField(default=True)),
                ('friendCount', models.BooleanField(default=True)),
                ('user', models.OneToOneField(related_name='infoDispaly', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInteresting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interesting', models.ForeignKey(to='userManager.Interesting')),
                ('userInfo', models.ForeignKey(to='userManager.UserInformation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSecurity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isLock', models.BooleanField(default=False)),
                ('LoginFailTime', models.IntegerField(default=0)),
                ('PasswordQuestion1', models.CharField(max_length=50, null=True, blank=True)),
                ('PasswordAnswer1', models.CharField(max_length=50, null=True, blank=True)),
                ('PasswordQuestion2', models.CharField(max_length=50, null=True, blank=True)),
                ('PasswordAnswer2', models.CharField(max_length=50, null=True, blank=True)),
                ('PasswordQuestion3', models.CharField(max_length=50, null=True, blank=True)),
                ('PasswordAnswer3', models.CharField(max_length=50, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='interest',
            field=models.ManyToManyField(to='userManager.Interesting', null=True, through='userManager.UserInteresting', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='user',
            field=models.OneToOneField(related_name='information', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
