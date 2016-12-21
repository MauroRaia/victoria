# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viapublica_app', '0005_auto_20161028_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='reclamo',
            name='seccion',
            field=models.ForeignKey(blank=True, to='viapublica_app.Seccion', null=True),
        ),
    ]
