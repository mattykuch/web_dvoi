# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_date_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='aobcg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aohepb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aohpv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aomeasles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aoopv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aopcv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aott',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='aoyf',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='commbcg',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commhepb',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commhpv',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commmeasles',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commopv',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commpcv',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commtt',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='commyf',
            field=models.CharField(max_length=500, default='Add comment here'),
        ),
        migrations.AddField(
            model_name='order',
            name='dateof_submit',
            field=models.DateTimeField(default='01/01/2017'),
        ),
        migrations.AddField(
            model_name='order',
            name='oqbcg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqhepb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqhpv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqmeasles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqopv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqpcv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqtt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='oqyf',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbbcg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbhepb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbhpv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbmeasles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbopv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbpcv',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbtt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='sbyf',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(max_length=50, default='e.g. Abim'),
        ),
        migrations.AlterField(
            model_name='order',
            name='month',
            field=models.CharField(max_length=50, default='e.g. January'),
        ),
        migrations.AlterField(
            model_name='order',
            name='submitter',
            field=models.CharField(max_length=50, default='e.g. Elton John Mabirizi'),
        ),
        migrations.AlterField(
            model_name='order',
            name='title_submitter',
            field=models.CharField(max_length=50, default='e.g. DCCT'),
        ),
    ]
