from core.sitemaps import CoreSitemapModels
from .models import Section
from .views import post_filter


class SectionSitemap(CoreSitemapModels):

    def items(self):
        return Section.objects.all()


class SectionPostSitemap(CoreSitemapModels):

    def items(self):
        return post_filter
