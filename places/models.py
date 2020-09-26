from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description_short = models.TextField(blank=True, verbose_name="Краткое описание")
    description_long = HTMLField(blank=True, verbose_name="Подробное описание")
    longitude = models.FloatField(verbose_name="Долгота")
    latitude = models.FloatField(verbose_name="Широта")
    place_id = models.CharField(max_length=20, verbose_name="Уникальный заголовок")
    
    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="places_images", blank=True, verbose_name="Файл изображения")
    place_image = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_image", verbose_name="Изображение")
    position = models.PositiveIntegerField(default=0, verbose_name="Порядковый номер")

    def __str__(self):
        return f"{self.position} {self.place_image}"

    class Meta(object):
        ordering = ['position']