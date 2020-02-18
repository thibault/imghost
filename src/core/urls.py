from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from images.views import list as view_list

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_list, name='image_list'),
    path('images/', include('images.urls')),
    path('memes/', include('memes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
