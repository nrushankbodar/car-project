# Generated by Django 5.0 on 2023-12-05 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0053_dealership_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owned_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car_owned', to='store.carowner'),
            preserve_default=False,
        ),
    ]
