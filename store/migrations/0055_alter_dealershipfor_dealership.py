# Generated by Django 5.0 on 2023-12-05 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0054_alter_car_owned_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealershipfor',
            name='dealership',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.dealership'),
        ),
    ]
