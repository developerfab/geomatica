# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151115_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=200)),
                ('latitud', models.FloatField(default=0.0)),
                ('longitud', models.FloatField(default=0.0)),
            ],
        ),
        migrations.AlterField(
            model_name='hueco',
            name='foto',
            field=models.ImageField(upload_to=b'hueco'),
        ),
    ]
