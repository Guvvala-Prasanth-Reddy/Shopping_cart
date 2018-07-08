from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
	return render(request,'base.html',{})	

def contact(request):
	return render(request,'contact.html',{})
def about (request):
	return render(request,'about.html',{})	
