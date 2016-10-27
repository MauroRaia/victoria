# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viapublica_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='latitud',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reclamo',
            name='longitus',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]
