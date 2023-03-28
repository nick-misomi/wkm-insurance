from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('newsletter/', views.home, name='home'),
    path('validate/', views.validate_email, name='validate_email'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
