# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-03 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('coures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coures.CourseList',
                                    verbose_name='\u6240\u5c5e\u8bfe\u7a0b'),
        ),
    ]
