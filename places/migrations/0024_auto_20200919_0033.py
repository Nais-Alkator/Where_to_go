# Generated by Django 3.0.7 on 2020-09-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0023_auto_20200919_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]