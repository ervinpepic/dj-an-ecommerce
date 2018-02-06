##Django imports
from django.db import models


##Other Imports


#Model class definition
class Product(models.Model):
	title 			= models.CharField(max_length=120)
	description 	= models.TextField()
	price 			= models.DecimalField(max_digits=20, decimal_places=2, default=29.99)

	##class methods
	def __str__(self):
		return self.title
