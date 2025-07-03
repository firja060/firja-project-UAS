# news/urls.py
from django.urls import path
from . import views
from news.views import tambah_berita

urlpatterns = [
    path('', views.home, name='home'),
    path('berita/<int:pk>/', views.berita_detail, name='berita_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/tambah/', tambah_berita, name='tambah_berita'),
]
