from django.conf.urls import patterns, url


urlpatterns = patterns(
    'images.views',
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^(?P<unique_key>\w+)/$', 'detail', name='detail'),
)
