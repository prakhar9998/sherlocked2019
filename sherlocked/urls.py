from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('play/', views.play, name='play'),
    path('submit', views.submit, name='submit'),
]