
from django.conf.urls import url

from splat.views import splat_list, splat_detail

urlpatterns = [
    url(r'/(?P<splat_id>\d+)/$', splat_detail),
    url(r'/$', splat_list),
]
