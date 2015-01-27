# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManager', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FriendsCategories',
        ),
        migrations.DeleteModel(
            name='FriendsInUserCategories',
        ),
        migrations.RemoveField(
            model_name='userfriends',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='userfriends',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFriends',
        ),
    ]
