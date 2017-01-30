# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_dateof_submit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='aobcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aohepb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aohpv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aomeasles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aoopv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aopcv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aott',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='aoyf',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqbcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqhepb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqhpv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqmeasles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqopv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqpcv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqtt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='oqyf',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbbcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbhepb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbhpv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbmeasles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbopv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbpcv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbtt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sbyf',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
