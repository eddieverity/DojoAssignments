# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='number_enrolled',
            field=models.IntegerField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]