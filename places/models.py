from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    short_description = models.TextField(
        blank=True, verbose_name="Краткое описание")
    long_description = HTMLField(blank=True, verbose_name="Подробное описание")
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")
    place_id = models.CharField(
        max_length=20, verbose_name="Уникальный заголовок")

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(
        upload_to="places_images", verbose_name="Файл изображения")
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="pictures", verbose_name="Изображение")
    position = models.IntegerField(default=1, verbose_name="Порядковый номер")

    def __str__(self):
        return f"{self.position} {self.place}"

    class Meta(object):
        ordering = ['position']
