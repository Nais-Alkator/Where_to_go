# Generated by Django 3.0.7 on 2020-09-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200906_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True),
        ),
    ]
