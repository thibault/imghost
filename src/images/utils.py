from os.path import splitext
import requests
from cStringIO import StringIO
from os.path import basename
from PIL import Image

from django.core.files.images import ImageFile


def download_image(url):
    r = requests.get(url)
    name = basename(url)
    img_temp = StringIO(r.content)
    image = ImageFile(img_temp, name=name)

    return image


def create_thumb(image, size):
    _basename, ext = splitext(image.name)
    ext = '.jpeg' if ext == '.jpg' else ext
    ext = ext[1:]

    thumbnail = Image.open(image.file.name)
    thumbnail.seek(0)
    thumbnail.thumbnail(size, Image.ANTIALIAS)

    tmp_file = StringIO()
    thumbnail.save(tmp_file, ext)
    return ImageFile(tmp_file)
