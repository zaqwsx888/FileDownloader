from rest_framework.viewsets import ModelViewSet
from .serializers import FilesSerializer
from .models import File


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FilesSerializer

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')


# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class FileView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     def get(self, request):
#         files = File.objects.all()
#         return Response({'files': FilesSerializer(files, many=True).data})
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = FilesSerializer(data=request.data)
#         if file_serializer.is_valid(raise_exception=True):
#             file_serializer.save()
#             return Response(
#               file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#               file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

