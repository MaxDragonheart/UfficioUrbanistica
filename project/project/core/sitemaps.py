from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse


class CoreSitemap(Sitemap):
    """
    Generic Sitemap class.
    """
    pass


class CoreSitemapModels(CoreSitemap):
    """
    Sitemap class for models.
    """

    def lastmod(self, obj):
        return obj.updating_date


class StaticSitemap(CoreSitemap):

    def items(self):
        staticpages = []

        staticpages.append("all_posts")  # app_section
        staticpages.append("open-geodata")  # app_opengeodata

        return staticpages

    def location(self, item):
        return reverse(item)


class FlatpageSitemap(CoreSitemap):

    def items(self):
        return FlatPage.objects.all()
