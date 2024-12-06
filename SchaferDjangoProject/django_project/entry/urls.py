from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='entries-home'),
    path('about/', views.about, name='entries-about'),
]
