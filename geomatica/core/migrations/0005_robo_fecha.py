# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151125_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='robo',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
