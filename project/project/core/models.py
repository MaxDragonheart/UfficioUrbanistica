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
    title = models.CharField(max_length=250, blank=False, null=False)
    subtitle = models.CharField(max_length=250, blank=False, null=False)
    logo = models.ImageField(upload_to='uploads/site', blank=False, null=False)
    header_image = models.ImageField(upload_to='uploads/site', blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    contacts = tinymce_models.HTMLField(blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Personalizza il sito"
        verbose_name_plural = "Personalizza il sito"
