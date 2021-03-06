from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from file_downloader import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('app_downloader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
