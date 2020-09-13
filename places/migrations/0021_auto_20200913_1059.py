# Generated by Django 3.0.7 on 2020-09-13 07:59

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0020_place_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='content',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
    ]
