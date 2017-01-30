# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20170127_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateof_submit',
            field=models.DateField(default=datetime.date(2017, 1, 27)),
            preserve_default=False,
        ),
    ]
