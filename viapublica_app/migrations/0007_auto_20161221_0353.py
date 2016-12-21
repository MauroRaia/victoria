# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viapublica_app', '0006_auto_20161220_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamo',
            name='seccion',
            field=models.ForeignKey(default='', blank=True, to='viapublica_app.Seccion'),
        ),
    ]
