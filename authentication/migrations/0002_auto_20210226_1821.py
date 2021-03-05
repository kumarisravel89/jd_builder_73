# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpasswordtable',
            old_name='Password',
            new_name='Password1',
        ),
        migrations.AddField(
            model_name='userpasswordtable',
            name='Password2',
            field=models.CharField(max_length=20, default=1),
            preserve_default=False,
        ),
    ]
