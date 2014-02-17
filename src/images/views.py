from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to

from images.forms import UploadForm
from images.utils import download_image
from images.models import Image


@render_to('upload.html')
def upload(request):
    form = UploadForm(request.POST or None)

    if form.is_valid():
        url = form.cleaned_data['url']
        image_file = download_image(url)

        image = Image.objects.create(
            image=image_file,
            source=url,
        )

        return redirect(image.get_absolute_url())

    return {
        'form': form,
    }


@render_to('list.html')
def list(request):
    pass


@render_to('detail.html')
def detail(request, unique_key):
    image = get_object_or_404(Image, unique_key=unique_key)
    full_url = request.build_absolute_uri(image.get_absolute_url())

    return {
        'image': image,
        'full_url': full_url,
    }
