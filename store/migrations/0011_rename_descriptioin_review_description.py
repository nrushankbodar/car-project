# Generated by Django 4.2.7 on 2023-11-27 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_discriptioin_review_descriptioin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='descriptioin',
            new_name='description',
        ),
    ]
