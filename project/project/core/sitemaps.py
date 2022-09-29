from django.contrib.sitemaps import ping_google, Sitemap
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse


class CoreSitemap(Sitemap):
    """
    Generic Sitemap class.
    """
    protocol = "https"

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
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
