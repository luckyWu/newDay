# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181024_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=10)),
                ('stu', models.ManyToManyField(to='app.Student')),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]
