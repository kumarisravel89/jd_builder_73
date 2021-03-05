# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210303_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpasswordtable',
            name='UserId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
