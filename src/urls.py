"""researchapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

# by default redirect to admin
# https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#reversing-admin-urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^old/', include('researchapp.urls')),
    url(r'^', include('portfolioapp.urls')),
    # url(r'^', RedirectView.as_view(
    #     pattern_name='admin:index', permanent=False)),
]
