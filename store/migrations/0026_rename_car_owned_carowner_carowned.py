# Generated by Django 4.2.7 on 2023-11-29 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_carowner_car_owned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carowner',
            old_name='car_owned',
            new_name='carowned',
        ),
    ]
