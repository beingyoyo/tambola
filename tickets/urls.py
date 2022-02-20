from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('ticket/', views.ticket, name='ticket'),
    path('admin/', views.admin, name='admin')
]
