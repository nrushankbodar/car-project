# Generated by Django 4.2.7 on 2023-12-04 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_car_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='carowner',
        ),
    ]
