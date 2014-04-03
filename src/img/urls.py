from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'images.views.list', name='image_list'),
    url(r'^images/', include('images.urls')),
    url(r'^memes/', include('memes.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
