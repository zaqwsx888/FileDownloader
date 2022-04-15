from rest_framework import serializers
from .models import File
from file_downloader.settings import MEDIA_ROOT
import os


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
        read_only_fields = ('id', 'size', 'file_extensions', 'time_create')

    @classmethod
    def handle_uploaded_file(cls, file):
        absolute_file_path = os.path.join(MEDIA_ROOT, 'Files', file.name)
        relative_file_path = os.path.join('Files', file.name)
        with open(absolute_file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return relative_file_path

    def create(self, validated_data):
        return File.objects.create(
            name=validated_data['name'],
            file=self.handle_uploaded_file(validated_data['file']),
            size=validated_data['file'].size,
            file_extensions=validated_data['file'].name.split('.')[-1]
        )
