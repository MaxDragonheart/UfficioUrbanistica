from core.feed import Atom1Feed, BaseRssSiteNewsFeed

from .models import Section
from .views import post_filter


class SectionRssSiteNewsFeed(BaseRssSiteNewsFeed):

    def get_object(self, request, slug_category, **kwargs):
            category = Section.objects.get(slug_category=slug_category)
            return category

    def items(self, item):
        return post_filter.filter(category=item).order_by('-publishing_date')[:5]


class SectionAtomSiteNewsFeed(SectionRssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = SectionRssSiteNewsFeed.description
