# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_userfollowers_userfollows'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollows',
            unique_together=set([('user', 'follow')]),
        ),
    ]
