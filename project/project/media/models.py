from django.db import models
from django.urls import reverse

from abstracts.models import FileUploadBase


class FileUpload(FileUploadBase):
    """
    Modello per l'upload di un file
    """
    file = models.FileField(upload_to='uploads/documents/%Y/%m/%d')
    highlighted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("single_file", kwargs={"pk": self.pk})

    @property
    def url_path(self):
        return self.file.url

    class Meta:
        ordering = ['name']
        verbose_name = "Documento"
        verbose_name_plural = "Documenti"

