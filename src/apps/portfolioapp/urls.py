from django.conf.urls import url
from django.views.generic import RedirectView

from . import views
from . import views_pubs
from . import views_seo

from researchapp.feeds import LatestPubsFeed

# urlpatterns = [
#     # ...
#     path('latest/feed/', LatestEntriesFeed()),
#     # ...
# ]


app_name = 'portfolioapp'
urlpatterns = [
    # url(r'^static/(?P<filename>[\w\-]+)',
    #     views.straight_to_template,
    #     name='straight_to_template'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<namedetail>[\w-]+)/$', views.projects, name='projects-detail'),

    # pubs section
    url(r'^words/$', views_pubs.words, name='words'),
    url(r'^papers/$', views_seo.section_redirect, {'target': '/words/'}, name='papers'), # legacy links
    url(r'^blog/$', views_seo.section_redirect, {'target': '/words/'}, name='blogs'),
    url(r'^papers/(?P<year>[\w-]+)/(?P<month>[\w-]+)/(?P<day>[\w-]+)/(?P<namedetail>[\w-]+)/$', views_pubs.paper_detail, name='papers-detail'),
    url(r'^blog/(?P<year>[\w-]+)/(?P<month>[\w-]+)/(?P<day>[\w-]+)/(?P<namedetail>[\w-]+)/$', views_pubs.blog_detail, name='blogs-detail'),
    
    # feeds
    url('^latest/feed/$', LatestPubsFeed(), name='words-feed-legacy'),
    url(r'^feed\.xml$', LatestPubsFeed(), name='words-feed'),
    # redirect 
    url(r'^quotes/$', RedirectView.as_view(url='https://quotes.michelepasin.org')),

    # rest 
    url(r'^sounds/$', views.sounds, name='music'),
    url(r'^sounds/(?P<namedetail>[\w-]+)/$', views.sounds, name='music-detail'),
    url(r'^events/', views.events, name='events'),
    # url(r'^photos/', views.photos, name='photos'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^$', views.home, name='home'),
    url(r'^robots\.txt$', views_seo.robots_txt, name='robots'),
    url(r'^sitemap\.xml$', views_seo.sitemap_xml, name='sitemap'),
]

