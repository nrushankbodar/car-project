# Generated by Django 5.0 on 2023-12-05 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('store', '0051_carwithdealership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='dealership_name',
        ),
        migrations.RemoveField(
            model_name='dealership',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='dealership',
            name='object_id',
        ),
        migrations.AddField(
            model_name='dealer',
            name='dealership',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dealers', to='store.dealership'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealership',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealership',
            name='ratings',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dealership',
            name='dealership_name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='DealerShipFor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.dealer')),
            ],
        ),
    ]
