from django.urls import path
from . import views

urlpatterns = [
    path('seoservices/', views.seo, name="seo"),
    path('localseo/', views.localseo, name="localseo"),
    path('linkbuilding/', views.linkbuilding, name="linkbuilding"),
    path('contentwriting/', views.contentwriting, name="contentwriting"),
    path('ecommerceseo/', views.ecommerceseo, name="ecommerceseo"),
    path('emailmarketing/', views.emailmarketing, name="emailmarketing"),
    path('ppc/', views.ppc, name="ppc"),
    path('asoservices/', views.aso, name="aso"),
    path('smoservices/', views.smo, name="smo"),
]
