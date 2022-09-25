from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from tinymce import models as tinymce_models

from abstracts.models import TimeManager


class SiteCustomization(TimeManager):
    """
    SiteCustomization Model inherits Site(django.contrib.sites.models) and TimeManager for
    create the informations useful to describe the website.
    """
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="related_site", default=1)
    site_title = models.CharField(max_length=250, blank=False, null=False)
    site_subtitle = models.CharField(max_length=250, blank=False, null=False)
    site_logo = models.ImageField(upload_to=settings.STATICFILES_DIRS, blank=False, null=False)
    site_description = models.CharField(max_length=100, blank=False, null=False)
    contacts = tinymce_models.HTMLField(blank=False, null=False)

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = "Personalizza il sito"
        verbose_name_plural = "Personalizza il sito"
