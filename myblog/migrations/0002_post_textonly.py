# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='textonly',
            field=models.TextField(default=datetime.datetime(2017, 1, 4, 1, 34, 34, 862679, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
