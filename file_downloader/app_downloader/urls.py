from django.conf.urls import url
from .views import FileViewSet

urlpatterns = [
    url(r'^upload/$', FileViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='file_upload'),
]
