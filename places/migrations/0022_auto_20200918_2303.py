# Generated by Django 3.0.7 on 2020-09-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0021_auto_20200913_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(blank=True, default=0, max_length=20),
        ),
    ]