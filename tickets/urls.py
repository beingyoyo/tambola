from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('ticket/', views.ticket, name='ticket'),
    path('number_generator/', views.number_generator, name='number_generator')
]
