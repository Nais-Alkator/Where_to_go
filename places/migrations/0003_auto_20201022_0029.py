# Generated by Django 3.0.7 on 2020-10-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20201022_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Порядковый номер'),
        ),
    ]
