# Generated by Django 4.2.7 on 2023-11-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_car_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='price',
            new_name='origenal_price',
        ),
        migrations.AddField(
            model_name='car',
            name='selling_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
