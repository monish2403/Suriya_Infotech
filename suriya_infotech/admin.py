from django.contrib import admin
from .models import Laptop, Desktop, Refurbished_Laptop, Refurbished_Desktop

# Register your models here.
admin.site.register(Laptop)
admin.site.register(Desktop)
admin.site.register(Refurbished_Laptop)
admin.site.register(Refurbished_Desktop)