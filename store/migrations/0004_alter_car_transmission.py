# Generated by Django 4.2.7 on 2023-11-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Autometic', 'Autometic'), ('Menual', 'Menual')], max_length=255),
        ),
    ]
