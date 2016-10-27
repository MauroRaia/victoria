# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viapublica_app', '0002_auto_20161017_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reclamo',
            old_name='longitus',
            new_name='longitud',
        ),
    ]
