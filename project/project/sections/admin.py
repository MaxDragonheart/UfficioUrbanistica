from django.contrib import admin

from .models import Section, SectionPost


class SectionAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
    prepopulated_fields = {"slug_category": ("category_name",)}
    fieldsets = [
                ("Dati generali", {"fields": ["category_name", "slug_category"]}),
            ]

    class Meta:
        model = Section


class SectionPostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "publishing_date", "updating_date", "highlighted", "draft", "is_future"]
    list_filter = ["publishing_date", "updating_date", "category"]
    search_fields = ["title", "description", "contents"]
    prepopulated_fields = {"slug_post": ("title",)}
    fieldsets = [
        ("Dati generali", {"fields": ["title", "slug_post", "header_image"]}),
        ("Contenuti", {"fields": ["description", "contents"]}),
        ("Riferimenti", {"fields": ["publishing_date", "category"]}),
        ("Opzioni", {"fields": ["highlighted", "draft"]}),
    ]

    class Meta:
        model = SectionPost


admin.site.register(Section, SectionAdmin)
admin.site.register(SectionPost, SectionPostAdmin)
