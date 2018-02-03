from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
	name = models.CharField(max_length=120)
	Location = models.CharField(max_length=120,null=True,blank=True)
	category = models.CharField(max_length=120,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
