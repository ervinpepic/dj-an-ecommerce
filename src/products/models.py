##Django imports
from django.db import models
import random
import os

##Other Imports

#image uploading functions for renaming
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	# print(instance)
	# print(filename)
	new_filename = random.randint(1,12312312)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename) 

class ProductManager(models.Manager):
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
		if qs.count() == 1:
			return qs.first()
		return None
#Model class definition
class Product(models.Model):
	title 			= models.CharField(max_length=120)
	description 	= models.TextField()
	price 			= models.DecimalField(max_digits=20, decimal_places=2, default=29.99)
	image 			= models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	#calling model managers
	objects = ProductManager()

	##class methods
	def __str__(self):
		return self.title
