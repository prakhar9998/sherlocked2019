from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('play/', views.play, name='play'),
    path('submit', views.submit, name='submit'),
    path('winner/', views.winner, name='winner'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('rules/', TemplateView.as_view(template_name='sherlocked/rules.html')),
    path('description/', TemplateView.as_view(template_name='sherlocked/about.html'))
]
