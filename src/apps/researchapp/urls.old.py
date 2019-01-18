from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

# urls for researcher app
urlpatterns = patterns(
    '',
    (r'^' + prefix + 'admin/', include(
        admin.site.urls)),  # <=== NEW SYNTAX				 
    # AJAX
    url(r'^newsfeed$',
        'researchapp.views.ajax_get_newsfeed',
        name='get_newsfeed'),
    url(r'^ajax_get_blogs$',
        'researchapp.views.ajax_get_blogs',
        name='ajax_get_blogs'),

    # MAIN
    (r'^' + prefix + '$', 'researchapp.views.dispatcher'),
    (r'^' + prefix + 'papers/feed/$', LatestPubsFeed()),
    (r'^' + prefix + 'videos/feed/$', LatestVideosFeed()),
    (r'^' + prefix + 'music/feed/$', LatestMusicFeed()),
    (r'^' + prefix + 'software/feed/$', LatestSoftwareFeed()),
    (r'^' + prefix + 'projects/feed/$', LatestProjectFeed()),

    # finally, the dynamic dispatcher
    url(r'^' + prefix + '(?P<pagename>\w+)/$',
        'researchapp.views.dispatcher',
        name='page_dispatcher'),
    url(r'^' + prefix + '(?P<pagename>\w+)/(?P<namedetail>\w+)/$',
        'researchapp.views.dispatcher',
        name='detail_page_dispatcher'),
)