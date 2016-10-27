# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viapublica_app', '0003_auto_20161017_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
