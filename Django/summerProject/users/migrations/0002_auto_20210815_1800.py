# Generated by Django 3.0 on 2021-08-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fare_status',
            field=models.CharField(blank=True, default='adult', max_length=500),
        ),
    ]