# Generated by Django 3.0.7 on 2020-09-12 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0018_place_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_image', to='places.Place'),
        ),
    ]