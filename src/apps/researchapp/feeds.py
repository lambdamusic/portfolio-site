from django.contrib.syndication.views import Feed
from researchapp.models import *
from django.urls import reverse
from datetime import datetime, time

from researchapp.management.commands.do_blogs_reindex import parse_markdown
from settings import BLOGS_ROOT


class LatestPubsFeed(Feed):
	title = "The news feed of www.michelepasin.org"
	link = "http://www.michelepasin.org/words/"
	description = "Latest articles, blogs posts and news"

	def items(self):
		return Publication.objects.exclude(
			isforthcoming=True).exclude(review=True).order_by('-pubdate')[:20]

	def item_title(self, item):
		return str(item.title)

	def item_description(self, item):
		if "blog" in item.pubtype.name.lower():
			TITLE, DATE, REVIEW, PURE_MARKDOWN = parse_markdown(BLOGS_ROOT + item.md_file)
			return str(PURE_MARKDOWN)[:1000] + " ..."
		else:
			return str(item.abstract)

	def item_pubdate(self, item):
		# trick cause syndication requires datetime objects, while we have date objects only
		#  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
		return datetime.combine(item.pubdate, time())

	def item_link(self, item):
		url = item.get_absolute_url()
		# NOTE hardcode url to avoid localhost interference
		return "https://www.michelepasin.org" + url


# class LatestVideosFeed(Feed):
#     title = "Michelepasin.org videos news feed"
#     link = "http://www.michelepasin.org/videos/"
#     description = "Updates on latest videos "

#     def items(self):
#         return Item.objects.filter(
#             atype__name__iexact="video").order_by('-date')[:10]

#     def item_title(self, item):
#         return str(item.title)

#     def item_description(self, item):
#         return str(item.description)

#     def item_pubdate(self, item):
#         # trick cause syndication requires datetime objects, while we have date objects only
#         #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
#         return datetime.combine(item.date, time())

#     def item_link(self, item):
#         return str("http://www.michelepasin.org/videos/%s/" % item.urlstub)


# class LatestMusicFeed(Feed):
#     title = "Michelepasin.org music news feed"
#     link = "http://www.michelepasin.org/music/"
#     description = "Updates on latest music "

#     def items(self):
#         return Item.objects.filter(
#             atype__name__in=["music", "livecoding", "performance"]).order_by(
#                 '-date')[:10]

#     def item_title(self, item):
#         return str(item.title)

#     def item_description(self, item):
#         return str(item.description)

#     def item_pubdate(self, item):
#         # trick cause syndication requires datetime objects, while we have date objects only
#         #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
#         return datetime.combine(item.date, time())

#     def item_link(self, item):
#         return str("http://www.michelepasin.org/music/%s/" % item.urlstub)


# class LatestSoftwareFeed(Feed):
#     title = "Michelepasin.org software news feed"
#     link = "http://www.michelepasin.org/software/"
#     description = "Updates on ..... "

#     def items(self):
#         return Software.objects.all().order_by('-date')[:10]

#     def item_title(self, item):
#         return str(item.title)

#     def item_description(self, item):
#         return str(item.short_title)

#     def item_pubdate(self, item):
#         # trick cause syndication requires datetime objects, while we have date objects only
#         #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
#         return datetime.combine(item.date, time())

#     def item_link(self, item):
#         return str("http://www.michelepasin.org/software/%s/" % item.urlstub)


# class LatestProjectFeed(Feed):
#     title = "Michelepasin.org project news feed"
#     link = "http://www.michelepasin.org/projects/"
#     description = "Updates on ..... "

#     def items(self):
#         return Project.objects.all().order_by('-dateto')[:10]

#     def item_title(self, item):
#         return str(item.title)

#     def item_description(self, item):
#         return str(item.short_title)

#     def item_pubdate(self, item):
#         # trick cause syndication requires datetime objects, while we have date objects only
#         #  http://stackoverflow.com/questions/7219599/django-feed-framework-tzinfo-error
#         return datetime.combine(item.dateto, time())

#     def item_link(self, item):
#         return str("http://www.michelepasin.org/projects/%s/" % item.urlstub)
