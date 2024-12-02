from django.contrib import admin
from django.urls import include, path
from cliente import views

urlpatterns = [
    path('Registro/',views.Registro,name='Registro'),
    path('homepag/',views.homepag,name='homepag'),
]