from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('play/', views.play, name='play'),
]