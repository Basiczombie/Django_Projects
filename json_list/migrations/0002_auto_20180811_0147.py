# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jfile',
            name='privacy',
            field=models.CharField(default='PUBLIC', choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], max_length=3),
        ),
    ]
