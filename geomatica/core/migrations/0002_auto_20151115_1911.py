# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hueco',
            name='latitud',
            field=models.BooleanField(default=0.0),
        ),
        migrations.AlterField(
            model_name='hueco',
            name='longitud',
            field=models.BooleanField(default=0.0),
        ),
    ]
