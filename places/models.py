from django.db import models

# Create your models here.

class Place(models.Model):
	title = models.CharField(max_length=200)
	description_short = models.TextField()
	description_long = models.TextField()
	longitude = models.FloatField()
	latitude = models.FloatField()

	def __str__(self):
		return self.title


class Image(models.Model):
	image = models.ImageField(blank=True)
	title = models.ForeignKey(Place, on_delete=models.CASCADE)
	image_id = models.AutoField(primary_key=True)

	def __str__(self):
		return f"{self.image_id} {self.title}"