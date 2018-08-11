# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_list', '0002_auto_20180811_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jfile',
            name='privacy',
            field=models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='PUBLIC', max_length=10),
        ),
    ]
