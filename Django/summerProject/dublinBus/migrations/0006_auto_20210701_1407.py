# Generated by Django 3.0 on 2021-07-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dublinBus', '0005_auto_20210701_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_stops',
            name='stop_lat',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='bus_stops',
            name='stop_lon',
            field=models.CharField(max_length=256),
        ),
    ]
