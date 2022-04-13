from rest_framework import serializers
from .models import File


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'id', 'name', 'file', 'size', 'file_extensions', 'time_create'
        )
        read_only_fields = ('id', 'size', 'file_extensions')

    def create(self, validated_data):
        return File.objects.create(
            **validated_data,
            size=validated_data['file'].size,
            file_extensions=validated_data['file'].name.split('.')[-1]
        )
