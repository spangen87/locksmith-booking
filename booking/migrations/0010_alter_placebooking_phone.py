# Generated by Django 3.2.15 on 2022-10-21 07:25

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placebooking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]