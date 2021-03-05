# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20210304_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpasswordtable',
            name='UserEmail',
            field=models.CharField(primary_key=True, max_length=50),
        ),
    ]
