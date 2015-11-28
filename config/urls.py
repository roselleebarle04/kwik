"""kwik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import settings
from ads import views as ad_views
from ads import urls as ad_urls
from accounts import views as account_views
from accounts import urls as account_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, {'template_name':'accounts/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name':'accounts/logout.html'}),
    url(r'^signup/$', account_views.signup, name='signup'),

    url(r'^', include(ad_urls)),
    url(r'^account/', include(account_urls, namespace='account')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
