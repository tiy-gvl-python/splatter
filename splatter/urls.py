"""splatter URL Configuration

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
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse_lazy

from splat import views as splat_views

urlpatterns = [
    url(r'^$', splat_views.splat_list, name="splat_list"),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, {'next_page': '/'}, name="logout"),

    url(r'^registration/', splat_views.user_registration, name="user_registration"),
    url(r'^splat_detail/(?P<splat_id>\d+)/$', splat_views.splat_detail, name="splat_detail"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user-detail/(?P<user_id>\d+)/$', splat_views.user_detail),
]

# joelIsAwesome
# JoelIsAwesome
