# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('district', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('submitter', models.CharField(max_length=50)),
                ('title_submitter', models.CharField(max_length=50)),
                ('date_submit', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to='account.Profile')),
            ],
        ),
    ]
