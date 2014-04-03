from django.conf.urls import patterns, url


urlpatterns = patterns(
    'memes.views',
    url(r'^(?P<unique_key>\w+)/(?P<top_text>[^,]+),(?P<bottom_text>[^\/]+)/$', 'meme', name='meme'),
)
