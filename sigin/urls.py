from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signedin', views.signedin, name='signedin'),
    path('home', views.home, name='home')
]
