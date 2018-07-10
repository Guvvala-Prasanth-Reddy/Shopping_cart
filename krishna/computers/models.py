from django.db import models

class LaptopTypes(models.Model):
	name   					=	models.CharField(max_length=150)
	Rating 					=	models.CharField(max_length=150 , null = True , blank = True )
	reviews					=	models.CharField(max_length=150 , null = True , blank = False)
	available_time			=	models.DateTimeField(auto_now = True , )
	expiry_time 			=	models.DateTimeField(auto_now_add=True)
	future_available_time	=	models.DateTimeField(auto_now = False , auto_now_add = False)

	def __str__(self):
		return self.name