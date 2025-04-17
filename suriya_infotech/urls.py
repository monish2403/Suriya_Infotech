from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('laptop/',views.view_laptop,name='laptop'),
    path('desktop/',views.view_desktop,name='desktop'),
    path('refurbished/',views.view_refurbished,name='refurbished'),
    path('printer/', views.view_printer, name='printer'),
    path('gaming/', views.view_gaming, name='gaming'),
    path('refurbished_laptop/', views.view_refurbished_laptop, name='refurbished_laptop'),
    path('refurbished_desktop/', views.view_refurbished_desktop, name='refurbished_desktop'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
