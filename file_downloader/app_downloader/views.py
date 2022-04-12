from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FileModel


class MyUploadView(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file = request.data['file']

        FileModel.my_file_field.save(file.name, file, save=True)
        return Response(status=status.HTTP_201_CREATED)
