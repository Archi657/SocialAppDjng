from django.urls import path
from . import views
urlpatterns = [
    path('', views.feed, name='feed'),
    path('', views.profile, name='profile'),
]