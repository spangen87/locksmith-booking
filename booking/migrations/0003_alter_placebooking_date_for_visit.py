# Generated by Django 3.2.15 on 2022-10-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_placebooking_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placebooking',
            name='date_for_visit',
            field=models.DateField(null=True),
        ),
    ]
