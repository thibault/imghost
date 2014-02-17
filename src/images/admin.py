from django.contrib import admin

from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('unique_key', 'image', 'extension')


admin.site.register(Image, ImageAdmin)
