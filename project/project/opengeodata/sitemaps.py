from core.sitemaps import CoreSitemapModels
from .models import Categories, OGCLayer, WebGISProject


class CategoriesSitemap(CoreSitemapModels):

    def items(self):
        return Categories.objects.all()


class OGCLayerSitemap(CoreSitemapModels):

    def items(self):
        return OGCLayer.objects.all()


class WebGISProjectSitemap(CoreSitemapModels):

    def items(self):
        return WebGISProject.objects.all()
