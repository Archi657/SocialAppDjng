from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='Social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Social/logout.html'), name='logout'),
]