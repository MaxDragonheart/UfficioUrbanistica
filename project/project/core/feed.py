from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed


class BaseRssSiteNewsFeed(Feed):
    title = "Nuova notizia online!"
    link = ""
    description = "Ultime news."

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.publishing_date

    def item_description(self, item):
        return item.description
