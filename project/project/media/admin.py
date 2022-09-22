from django.contrib import admin

from .models import FileUpload


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ["name", "size", "extension", "url_path", "publishing_date", "highlighted"]
    list_filter = ["publishing_date", "highlighted"]
    search_fields = ["name", "description"]

    class Meta:
        model = FileUpload


admin.site.register(FileUpload, FileUploadAdmin)
