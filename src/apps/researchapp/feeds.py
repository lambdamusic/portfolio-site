from django.contrib.syndication.views import Feed
from researchapp.models import *
from datetime import datetime, time

# from django.utils.encoding import str


class LatestPubsFeed(Feed):
    title = "Michelepasin.org publication news feed"
    link = "http://www.michelepasin.org/papers/"
    description = "Updates on ..... "

    def items(self):
        return Publication.objects.exclude(
            isforthcoming=True).order_by('-pubdate')[:10]

    def item_title(self, item):
        return str(item.title)

    def item_description(self, item):
        return str(item.pub_summary())

    def item_pubdate(self, item):
        # trick cause syndication requires datetime objects, while we have date objects only
        #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
        return datetime.combine(item.pubdate, time())

    def item_link(self, item):
        return str("http://www.michelepasin.org/papers/%s/" % item.id)


class LatestVideosFeed(Feed):
    title = "Michelepasin.org videos news feed"
    link = "http://www.michelepasin.org/videos/"
    description = "Updates on latest videos "

    def items(self):
        return Item.objects.filter(
            atype__name__iexact="video").order_by('-date')[:10]

    def item_title(self, item):
        return str(item.title)

    def item_description(self, item):
        return str(item.description)

    def item_pubdate(self, item):
        # trick cause syndication requires datetime objects, while we have date objects only
        #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
        return datetime.combine(item.date, time())

    def item_link(self, item):
        return str("http://www.michelepasin.org/videos/%s/" % item.urlstub)


class LatestMusicFeed(Feed):
    title = "Michelepasin.org music news feed"
    link = "http://www.michelepasin.org/music/"
    description = "Updates on latest music "

    def items(self):
        return Item.objects.filter(
            atype__name__in=["music", "livecoding", "performance"]).order_by(
                '-date')[:10]

    def item_title(self, item):
        return str(item.title)

    def item_description(self, item):
        return str(item.description)

    def item_pubdate(self, item):
        # trick cause syndication requires datetime objects, while we have date objects only
        #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
        return datetime.combine(item.date, time())

    def item_link(self, item):
        return str("http://www.michelepasin.org/music/%s/" % item.urlstub)


class LatestSoftwareFeed(Feed):
    title = "Michelepasin.org software news feed"
    link = "http://www.michelepasin.org/software/"
    description = "Updates on ..... "

    def items(self):
        return Software.objects.all().order_by('-date')[:10]

    def item_title(self, item):
        return str(item.title)

    def item_description(self, item):
        return str(item.short_title)

    def item_pubdate(self, item):
        # trick cause syndication requires datetime objects, while we have date objects only
        #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
        return datetime.combine(item.date, time())

    def item_link(self, item):
        return str("http://www.michelepasin.org/software/%s/" % item.urlstub)


class LatestProjectFeed(Feed):
    title = "Michelepasin.org project news feed"
    link = "http://www.michelepasin.org/projects/"
    description = "Updates on ..... "

    def items(self):
        return Project.objects.all().order_by('-dateto')[:10]

    def item_title(self, item):
        return str(item.title)

    def item_description(self, item):
        return str(item.short_title)

    def item_pubdate(self, item):
        # trick cause syndication requires datetime objects, while we have date objects only
        #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
        return datetime.combine(item.dateto, time())

    def item_link(self, item):
        return str("http://www.michelepasin.org/projects/%s/" % item.urlstub)
