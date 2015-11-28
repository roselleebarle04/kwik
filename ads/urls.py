from django.conf.urls import include, url
from django.contrib import admin

from . import views as ad_views

urlpatterns = [
	url(r'^$', ad_views.ad_timeline, name='timeline'),
	url(r'^info/$', ad_views.ad_info, name="ad_info"),
	url(r'^ad/create/$', ad_views.create_ad, name="create_ad"),
]
