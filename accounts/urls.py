from django.conf.urls import include, url
from django.contrib import admin

from . import views as account_views

urlpatterns = [
	url(r'^profile/$', account_views.profile, name='profile'),
	url(r'^settings/$', account_views.settings, name='settings'),
]
