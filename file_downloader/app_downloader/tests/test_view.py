from django.test import TestCase, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
import shutil
from ..models import File

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ViewsTest(TestCase):

    # Создание временной базы
    @classmethod
    def setUpTestData(cls):
        file = SimpleUploadedFile(
            'file_1.jpg', content=b'', content_type='image/jpg')
        File.objects.create(name='Test file 1', file=file)

    # Тесты проверки правильности url адреса
    def test_url_exist_at_desired_location(self):
        response = self.client.get(reverse('file_upload'))
        self.assertEqual(response.status_code, 200)

    # Тест загрузки файла
    def test_file_upload(self):
        data = {
            'name': 'Test file 2',
            'file': SimpleUploadedFile(
                'file_2.jpg',
                content=open(
                    'app_downloader/tests/test_file.jpg', 'rb').read(),
                content_type='image/jpeg')
        }
        self.assertTrue(File.objects.all().count() == 1)
        response = self.client.post(reverse('file_upload'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(File.objects.all().count() == 2)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT)
        super().tearDownClass()
