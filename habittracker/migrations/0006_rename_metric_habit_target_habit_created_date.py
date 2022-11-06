# Generated by Django 4.1.3 on 2022-11-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0005_rename_date_dailyrecord_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='metric',
            new_name='target',
        ),
        migrations.AddField(
            model_name='habit',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
