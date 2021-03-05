# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_userpasswordtable_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpasswordtable',
            name='id',
        ),
        migrations.AddField(
            model_name='userpasswordtable',
            name='UserName',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpasswordtable',
            name='UserId',
            field=models.CharField(primary_key=True, max_length=10, serialize=False),
        ),
    ]
