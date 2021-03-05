# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210226_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpasswordtable',
            name='Password2',
        ),
    ]
