# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_order_dateof_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='commmeasles',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
    ]
