# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hueco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=200)),
                ('latitud', models.IntegerField(default=0)),
                ('longitud', models.IntegerField(default=0)),
                ('foto', models.ImageField(upload_to=b'static/image_user/')),
            ],
        ),
        migrations.CreateModel(
            name='Trafico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zona', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(default=1)),
            ],
        ),
    ]
