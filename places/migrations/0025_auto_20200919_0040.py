# Generated by Django 3.0.7 on 2020-09-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0024_auto_20200919_0033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
        migrations.AddField(
            model_name='place',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
