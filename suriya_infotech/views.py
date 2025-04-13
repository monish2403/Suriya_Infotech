from django.shortcuts import render
from .models import laptop

# Create your views here.

def home(request):
    return render(request,'home.html')

def view_laptop(request):
    laptops = laptop.objects.all() 
    return render(request,'laptop.html',{'laptops': laptops})
