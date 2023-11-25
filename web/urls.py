from django.urls import path
from . import views

urlpatterns = [
    path('staticweb/', views.staticweb, name='staticweb'),
    path('ecommerceweb/', views.ecommerceweb, name='ecommerceweb'),
    path('webredesign/', views.webredesign, name='webredesign'),
    path('customweb/', views.customweb, name='customweb'),
    path('cmsbasedweb/', views.cmsbasedweb, name='cmsbasedweb'),
    path('pythondevelopment/', views.pythondevelopment, name='pythondevelopment'),
]
