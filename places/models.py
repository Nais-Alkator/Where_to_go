from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = HTMLField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    place_id = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="places_images", blank=True)
    place_image = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_image")
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f"{self.position} {self.place_image}"

    class Meta(object):
        ordering = ['position']