from os.path import splitext
import requests
from io import StringIO
from os.path import basename
from PIL import Image, ImageOps

from django.core.files.images import ImageFile


def download_image(url):
    r = requests.get(url)
    name = basename(url)
    img_temp = StringIO(r.content)
    image = ImageFile(img_temp, name=name)

    return image


def create_thumb(image, size):
    _basename, ext = splitext(image.name)
    ext = ext.lower()
    ext = '.jpeg' if ext == '.jpg' else ext
    ext = ext[1:]

    thumbnail = Image.open(image.file.name)

    if type(size) == tuple:
        thumbnail = ImageOps.fit(thumbnail, size, Image.ANTIALIAS)
    else:
        thumbnail.thumbnail((size, size), Image.ANTIALIAS)

    tmp_file = StringIO()
    thumbnail.save(tmp_file, ext, optimize=True)
    return ImageFile(tmp_file)
