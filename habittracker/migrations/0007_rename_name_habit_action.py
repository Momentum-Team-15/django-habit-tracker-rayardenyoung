# Generated by Django 4.1.3 on 2022-11-06 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0006_rename_metric_habit_target_habit_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='name',
            new_name='action',
        ),
    ]
