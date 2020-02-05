from django.db import models

class MovieRating(models.Model):
	title=models.CharField(max_length=100)
	rating=models.DecimalField(max_digits=2,decimal_places=1)
	year=models.CharField(max_length=4)


	def __str__(self):
		return self.title
