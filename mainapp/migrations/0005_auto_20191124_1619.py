# Generated by Django 2.2.6 on 2019-11-24 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_mainmodel_ph_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainmodel',
            name='energy_1',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='energy_2',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='energy_3',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='energy_4',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='energy_5',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='power_1',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='power_2',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='power_3',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='power_4',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='power_5',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='temp',
        ),
        migrations.RemoveField(
            model_name='mainmodel',
            name='time',
        ),
    ]
