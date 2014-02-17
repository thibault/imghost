from os.path import splitext
import random
import string
import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


def upload_path(instance, filename):
    date_path = datetime.datetime.today().strftime('%Y/%m')
    basename, ext = splitext(filename)
    unique_key = instance.get_unique_key()

    return 'images/%s/%s%s' % (
        date_path,
        unique_key,
        ext
    )


class Image(models.Model):
    """A single image file."""
    unique_key = models.CharField(
        _('Unique key'),
        max_length=20,
        unique=True)
    image = models.ImageField(
        _('Image file'),
        upload_to=upload_path,
        height_field='height',
        width_field='width')
    extension = models.CharField(
        _('Extension'),
        max_length=4,
        default='')
    height = models.PositiveIntegerField(
        _('Height'),
        default=0)
    width = models.PositiveIntegerField(
        _('Width'),
        default=0)
    source = models.URLField(
        _('Source'),
        null=True, blank=True)

    created_on = models.DateTimeField(
        _('Created on'),
        auto_now_add=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __unicode__(self):
        return '%s%s' % (self.unique_key, self.extension)

    def get_absolute_url(self):
        return reverse('detail', args=[self.unique_key])

    def save(self, *args, **kwargs):
        if not self.id:
            self.generate_unique_key()
            self.generate_extension()
        super(Image, self).save(*args, **kwargs)

    def get_unique_key(self):
        if not self.unique_key:
            self.generate_unique_key()

        return self.unique_key

    def generate_unique_key(self):
        key_chars = string.ascii_uppercase + string.digits
        self.unique_key = ''.join(random.choice(key_chars) for x in range(10))

    def generate_extension(self):
        name, ext = splitext(self.image.url)
        self.extension = ext
