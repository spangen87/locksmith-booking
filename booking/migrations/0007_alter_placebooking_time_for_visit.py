# Generated by Django 3.2.15 on 2022-10-19 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_placebooking_time_for_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placebooking',
            name='time_for_visit',
            field=models.TimeField(default=datetime.time(12, 0)),
        ),
    ]