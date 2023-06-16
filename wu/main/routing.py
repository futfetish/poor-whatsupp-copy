from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/ls/(?P<pk>\w+)/$', consumers.Ls.as_asgi()),
]