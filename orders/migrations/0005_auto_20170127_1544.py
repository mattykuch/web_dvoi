# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170127_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateof_submit',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
