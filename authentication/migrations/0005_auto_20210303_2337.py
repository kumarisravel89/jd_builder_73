# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210303_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpasswordtable',
            name='UserId',
            field=models.IntegerField(primary_key=True, max_length=10, serialize=False, auto_created=True),
        ),
    ]
