from django.shortcuts import get_object_or_404
from annoying.decorators import render_to

from images.models import Image
from memes.utils import draw_text


@render_to('meme.html')
def meme(request, unique_key, top_text, bottom_text):
    image = get_object_or_404(Image, unique_key=unique_key)

    img_file = draw_text(image.image.file, top_text, bottom_text)
    img_file.save('/tmp/meme.jpg')

    return {
        'image': image,
    }
