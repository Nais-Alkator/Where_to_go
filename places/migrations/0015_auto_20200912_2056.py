# Generated by Django 3.0.7 on 2020-09-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_auto_20200912_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
