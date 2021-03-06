##Django imports
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
import random
import os


##Other Imports
from .utils import unique_slug_generator

#image uploading functions for renaming
def get_filename_ext(putanjafajla):
	base_name = os.path.basename(putanjafajla)
	name, ext = os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, ime_fajla):
	new_filename = random.randint(1,12312312)
	name, ext = get_filename_ext(ime_fajla)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename) 

class ProductQuerySet(models.query.QuerySet):

	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True, active=True)

	def search(self, query):
		lookups = (
			Q(title__icontains=query) | 
			Q(description__icontains=query) |
    	    Q(price__icontains=query) |
            Q(tag__title__icontains=query)
        	)
		return self.filter(lookups).distinct()

class ProductManager(models.Manager):

	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def featured(self): #Product.objects.featured()
		return self.get_queryset().featured()

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
		if qs.count() == 1:
			return qs.first()
		return None

	def search(self, query):
		return self.get_queryset().active().search(query)

#Model class definition
class Product(models.Model):
	title 			= models.CharField(max_length=120)
	slug  			= models.SlugField(default='slug-url-share', blank=True, unique=True)
	description 	= models.TextField()
	price 			= models.DecimalField(max_digits=20, decimal_places=2, default=29.99)
	image 			= models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	featured 	    = models.BooleanField(default=False)
	active 			= models.BooleanField(default=True)
	timestamp 		= models.DateField(auto_now_add=True)

	#calling model managers
	objects = ProductManager()

	##class methods
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail", kwargs={"slug": self.slug})

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
