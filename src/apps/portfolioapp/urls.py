from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = 'portfolioapp'
urlpatterns = [
    # url(r'^static/(?P<filename>[\w\-]+)',
    #     views.straight_to_template,
    #     name='straight_to_template'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<namedetail>\w+)/$', views.projects, name='projects-detail'),
    url(r'^papers/$', views.papers, name='papers'),
    url(r'^papers/(?P<namedetail>\w+)/$', views.papers, name='papers-detail'),
    url(r'^sounds/$', views.sounds, name='music'),
    url(r'^sounds/(?P<namedetail>\w+)/$', views.sounds, name='music-detail'),
    url(r'^events/', views.events, name='events'),
    url(r'^photos/', views.photos, name='photos'),
    url(r'^about/bio/', views.bio, name='bio'),
    url(r'^about/', views.about, name='about'),
    url(r'^$', views.home, name='home'),
]

