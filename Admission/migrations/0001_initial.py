# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=100)),
                ('Stream', models.CharField(max_length=100)),
                ('Session', models.CharField(max_length=100)),
                ('Class', models.IntegerField(default=0)),
                ('Previous_Remark', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
