from django.conf.urls import patterns, url


urlpatterns = patterns(
    'memes.views',
    url(r'^(?P<unique_key>\w+)/$', 'meme', name='meme'),
)
