# Generated by Django 4.1.3 on 2022-11-05 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0003_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='created_date',
        ),
        migrations.AddField(
            model_name='habit',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='metric',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='unit_of_measure',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='habit',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='habittracker.habit'),
        ),
    ]
