# Generated by Django 3.2.15 on 2022-10-19 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placebooking',
            name='time_for_visit',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]