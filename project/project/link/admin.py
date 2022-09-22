from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "publishing_date", "updating_date", "column"]
    list_filter = ["column"]
    search_fields = ["title", "description"]

    class Meta:
        model = Link


admin.site.register(Link, LinkAdmin)
