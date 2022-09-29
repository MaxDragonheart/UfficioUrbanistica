from itertools import chain

from core.feed import Atom1Feed, BaseRssSiteNewsFeed

from .models import Categories, OGCLayer, WebGISProject


class CategoriesRssSiteNewsFeed(BaseRssSiteNewsFeed):

    def get_object(self, request, slug_category, **kwargs):
        category = Categories.objects.get(slug_category=slug_category)
        return category

    def items(self, item):
        wms = OGCLayer.objects.filter(categories=item).order_by('-publishing_date')
        webgis = WebGISProject.objects.filter(categories=item).order_by('-publishing_date')

        return list(chain(wms, webgis))[:5]


class CategoriesAtomSiteNewsFeed(CategoriesRssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = CategoriesRssSiteNewsFeed.description
