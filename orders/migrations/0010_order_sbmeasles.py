# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20170127_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sbmeasles',
            field=models.IntegerField(default=0),
        ),
    ]
