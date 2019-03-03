from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login', views.Login.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.Signup.as_view(), name='signup'),
    path('', login_required(TemplateView.as_view(template_name='sherlocked/about.html'),login_url='/login'))
]
