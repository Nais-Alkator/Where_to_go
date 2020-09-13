# Generated by Django 3.0.7 on 2020-09-06 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20200903_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_image', to='places.Place'),
        ),
    ]