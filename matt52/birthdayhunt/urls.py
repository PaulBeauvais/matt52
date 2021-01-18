from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hunt-home'),
    path('about/', views.about, name='hunt-about'),
    path('scavenges/', views.scavenges_view, name='hunt-scavenges'),
    path('photos/', views.photos_view, name='hunt-photos')
]