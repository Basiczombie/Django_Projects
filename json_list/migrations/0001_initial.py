# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('jfile', models.FileField(upload_to='json_files/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('privacy', models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], max_length=3)),
                ('user', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['upload_date'],
                'verbose_name_plural': 'jfiles',
            },
        ),
    ]
