# Generated by Django 3.0.7 on 2020-10-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.IntegerField(verbose_name='Порядковый номер'),
        ),
    ]
