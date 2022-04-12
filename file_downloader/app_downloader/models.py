import os
from django.db import models


class FileModel(models.Model):
    file = models.FileField(
        upload_to='Product_files/', verbose_name='Файлы',
    )
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата загрузки'
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.file.name

    def filename(self):
        return os.path.basename(self.file.path)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['id']

