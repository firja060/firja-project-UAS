# senblog/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import home
from news.views import register 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('news.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),  # ⬅️ Tambahkan ini
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
