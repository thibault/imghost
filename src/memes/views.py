from django.shortcuts import get_object_or_404
from annoying.decorators import render_to

from images.models import Image


@render_to('meme.html')
def meme(request, unique_key):
    image = get_object_or_404(Image, unique_key=unique_key)

    return {
        'image': image,
    }
