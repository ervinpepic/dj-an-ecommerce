from django.contrib import admin

#my module imports
from .models import Product

admin.site.register(Product)
