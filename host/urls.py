

from django.urls import path
from . import views
urlpatterns = [
    path('', views.demo, name='demo'),
    path('template/', views.template, name='template')
]