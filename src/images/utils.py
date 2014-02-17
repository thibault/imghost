import requests
from cStringIO import StringIO
from os.path import basename

from django.core.files.images import ImageFile


def download_image(url):
    r = requests.get(url)
    name = basename(url)
    img_temp = StringIO(r.content)
    image = ImageFile(img_temp, name=name)

    return image
