from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('battle/', views.battle, name='battle'),
    path('links/', views.links, name='links'),


]

 