from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('unique_key', 'image', 'extension')
    actions = ['make_thumbnails']

    def make_thumbnails(self, request, queryset):
        for img in queryset:
            img.generate_thumbnails()
    make_thumbnails.short_description = _('Regenerates thumbnails')



admin.site.register(Image, ImageAdmin)
