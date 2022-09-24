from django.contrib import admin

from .models import SiteCustomization


class SiteCustomizationAdmin(admin.ModelAdmin):

    class Meta:
        model = SiteCustomization


admin.site.register(SiteCustomization, SiteCustomizationAdmin)
