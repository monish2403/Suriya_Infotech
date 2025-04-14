from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('home/', views.home, name='home'),
    path('laptop/',views.view_laptop,name='laptop'),
    path('desktop/',views.view_desktop,name='desktop'),
    path('refurbished/',views.view_refurbished,name='refurbished'),
    path('printer/', views.view_printer, name='printer'),
    path('gaming/', views.view_gaming, name='gaming'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
