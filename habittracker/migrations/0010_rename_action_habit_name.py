# Generated by Django 4.1.3 on 2022-11-06 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0009_remove_dailyrecord_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='action',
            new_name='name',
        ),
    ]
