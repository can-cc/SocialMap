# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0004_auto_20150207_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollowers',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='userfollowers',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFollowers',
        ),
    ]
