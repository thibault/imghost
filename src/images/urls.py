from django.conf.urls import patterns, url


urlpatterns = patterns(
    'images.views',
    url(r'^$', 'upload', name='upload'),
)
