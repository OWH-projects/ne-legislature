from django.conf.urls import *

urlpatterns = patterns('',
    (r'^/bill/(?P<session>[0-9]+)/(?P<bill>[0-9]+)', 'myproject.neleg.views.Bill'),
    (r'^', 'myproject.neleg.views.Main'),
    )