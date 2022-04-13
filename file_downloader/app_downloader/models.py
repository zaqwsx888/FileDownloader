from django.db import models


class File(models.Model):
    name = models.CharField(max_length=140, verbose_name='Название файла')
    file = models.FileField(
        upload_to='Files/', verbose_name='Файл')
    size = models.IntegerField(
        default=0, editable=False, verbose_name='Размер')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['id']
