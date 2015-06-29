
from django.conf.urls import url

from splat.views import hello_world

urlpatterns = [
    url(r'^hello/', hello_world),
]
