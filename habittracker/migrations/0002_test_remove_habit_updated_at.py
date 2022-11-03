# Generated by Django 4.1.3 on 2022-11-03 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='habit',
            name='updated_at',
        ),
    ]