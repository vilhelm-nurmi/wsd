from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=255, unique = True)
	description = models.TextField()
	image_url = models.URLField(blank = True)
	quantity = models.IntegerField(default = 0)
	
	def sell(self):
		self.quantity -= 1
		self.save()
		