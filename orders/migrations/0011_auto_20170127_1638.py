# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_sbmeasles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='sbmeasles',
        ),
        migrations.AddField(
            model_name='order',
            name='dateof_submit',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
