from django.db import models
from django.contrib import admin


class Place(models.Model):
	title = models.CharField(max_length=200)
	description_short = models.TextField(blank=True)
	description_long = models.TextField(blank=True)
	longitude = models.FloatField()
	latitude = models.FloatField()
	place_id = models.CharField(max_length=20)

	def __str__(self):
		return self.title


class Image(models.Model):
	image = models.ImageField(blank=True)
	place_image = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_image")
	image_id = models.AutoField(primary_key=True)

	def __str__(self):
		return f"{self.image_id} {self.place_image}"


class ImageInline(admin.TabularInline):
    model = Image


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]