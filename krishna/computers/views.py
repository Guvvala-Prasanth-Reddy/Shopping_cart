from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .models import LaptopTypes

def Laptop_list(request):
	template_name='restaurants/restaurants.html'
	data = LaptopTypes.objects.all()
	context={
			"Home": data
	}		
	return render(request,template_name,context)
