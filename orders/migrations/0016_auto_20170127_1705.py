# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_remove_order_commmeasles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'OrderGeneralInfos', 'verbose_name': 'OrderGeneralInfo'},
        ),
    ]
