# Generated by Django 4.1.3 on 2022-11-06 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0008_remove_habit_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyrecord',
            name='created_date',
        ),
    ]
