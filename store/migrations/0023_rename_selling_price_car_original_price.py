# Generated by Django 4.2.7 on 2023-11-29 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_car_origenal_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='selling_price',
            new_name='original_price',
        ),
    ]
