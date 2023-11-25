from django.urls import path
from . import views

urlpatterns = [
    path('socialmedia/', views.socialmedia, name='socialmedia' ),
    path('fbadvertising/', views.fbadvertising, name='fbadvertising' ),
    path('twittera/', views.twittera, name='twittera'),
    path('linkedina/', views.linkedina, name='linkedina'),
    path('Instagramm/', views.Instagramm, name='Instagramm'),
    path('youtubem/', views.youtubem, name='youtubem'),
    path('ormservices/', views.ormservices, name='ormservices'),
]
