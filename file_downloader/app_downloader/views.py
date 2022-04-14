from rest_framework.viewsets import ModelViewSet
from .serializers import FilesSerializer
from .models import File


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesSerializer
