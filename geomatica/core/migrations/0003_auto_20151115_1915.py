# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151115_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hueco',
            name='latitud',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='hueco',
            name='longitud',
            field=models.FloatField(default=0.0),
        ),
    ]
