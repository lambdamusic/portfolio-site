from django.conf.urls import url
from django.views.generic import RedirectView

from . import views
from . import feeds

app_name = 'researchapp'
urlpatterns = [
    # url(r'^$', views.home, name='home'),

    # MAIN
    url(r'^$', views.dispatcher),
    #
    url(r'^papers/feed/$', feeds.LatestPubsFeed()),
    url(r'^videos/feed/$', feeds.LatestVideosFeed()),
    url(r'^music/feed/$', feeds.LatestMusicFeed()),
    url(r'^software/feed/$', feeds.LatestSoftwareFeed()),
    url(r'^projects/feed/$', feeds.LatestProjectFeed()),
    # AJAX
    url(r'^newsfeed$', views.ajax_get_newsfeed, name='get_newsfeed'),
    url(r'^ajax_get_blogs$', views.ajax_get_blogs, name='ajax_get_blogs'),
    # finally, the dynamic dispatcher
    url(r'^(?P<pagename>\w+)/$', views.dispatcher, name='page_dispatcher'),
    url(r'^(?P<pagename>\w+)/(?P<namedetail>\w+)/$',
        views.dispatcher,
        name='detail_page_dispatcher'),
]
