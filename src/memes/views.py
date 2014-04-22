import mimetypes
from django.shortcuts import get_object_or_404, redirect
from annoying.decorators import render_to

from images.models import Image
from memes.forms import MemeUploadForm


@render_to('meme.html')
def meme(request, unique_key):
    image = get_object_or_404(Image, unique_key=unique_key)
    mime = mimetypes.guess_type(image.image.url)[0]

    form = MemeUploadForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        img = Image.objects.create(
            image=data['file'],
            source='',
            extension='png',
            is_meme=True,
            source_image=data['source_image']
        )

        return redirect(img.get_absolute_url())

    return {
        'image': image,
        'mime': mime,
    }
