from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from annoying.decorators import render_to

from images.forms import UploadForm
from images.utils import download_image
from images.models import Image


@render_to('upload.html')
def upload(request):

    if not request.user.is_authenticated():
        raise PermissionDenied('Sorry, only the keymaster can do this.')

    form = UploadForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        url = form.cleaned_data['url']
        file = form.cleaned_data['file']
        image_file = file if file else download_image(url)

        image = Image.objects.create(
            image=image_file,
            source=url or '',
        )

        return redirect(image.get_absolute_url())

    return {
        'form': form,
    }


@render_to('list.html')
def list(request):
    images = Image.objects \
        .filter(is_meme=False) \
        .filter(hidden=False)
    form = UploadForm()

    return {
        'images': images,
        'form': form,
    }


@render_to('detail.html')
def detail(request, unique_key):
    qs = Image.objects.filter(hidden=False)
    image = get_object_or_404(qs, unique_key=unique_key)

    if image.is_meme:
        base_key = image.source_image.unique_key
    else:
        base_key = image.unique_key

    return {
        'image': image,
        'base_key': base_key,
        'related_memes': image.related_memes.all(),
        'has_memes': image.related_memes.all().count() > 0,
    }
