from django.db import models

# Create your models here.

class Place(models.Model):
	title = models.CharField(max_length=200)
	imgs = models.ImageField(blank=True)
	description_short = models.TextField()
	description_long = models.TextField()
	longitude = models.FloatField()
	latitude = models.FloatField()


	def __str__(self):
		return self.title