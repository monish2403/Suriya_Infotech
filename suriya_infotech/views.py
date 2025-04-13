from django.shortcuts import render
from .models import Laptop, Desktop

# Create your views here.

def home(request):
    return render(request,'home.html')

def view_laptop(request):
    laptops = Laptop.objects.all() 
    return render(request,'laptop.html',{'laptops': laptops})

def view_desktop(request):
    desktops = Desktop.objects.all() 
    return render(request,'desktop.html',{'desktops': desktops})
