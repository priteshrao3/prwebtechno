from django.urls import path
from . import views

urlpatterns = [
    path('androidapp/', views.androidapp, name='androidapp'),
    path('iphoneapp/', views.iphoneapp, name='iphoneapp'),
    path('ipadapp/', views.ipadapp, name='ipadapp'),
    path('hybridapp/', views.hybridapp, name='hybridapp'),
]
