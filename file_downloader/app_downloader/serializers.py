from rest_framework import serializers
from .models import File
from file_downloader.settings import MEDIA_ROOT


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
        read_only_fields = ('id', 'size', 'file_extensions', 'time_create')

    def handle_uploaded_file(self, file):
        absolute_file_path = '{0}/Files/{1}'.format(MEDIA_ROOT, file.name)
        relative_file_path = '/Files/{0}'.format(file.name)
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
