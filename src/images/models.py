from os.path import splitext
import random
import string

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from images.utils import create_thumb


upload_path = 'images/%Y/%m/'


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
    thumb_small = models.ImageField(
        _('Small thumbnail'),
        blank=True,
        upload_to=upload_path)
    thumb_large = models.ImageField(
        _('Large thumbnail'),
        blank=True,
        upload_to=upload_path)
    extension = models.CharField(
        _('Extension'),
        max_length=5,
        default='')
    height = models.PositiveIntegerField(
        _('Height'),
        default=0)
    width = models.PositiveIntegerField(
        _('Width'),
        default=0)
    source = models.URLField(
        _('Source'),
        max_length=2048,
        null=True, blank=True)

    created_on = models.DateTimeField(
        _('Created on'),
        auto_now_add=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ('-created_on',)

    def __unicode__(self):
        return '%s%s' % (self.unique_key, self.extension)

    def get_absolute_url(self):
        return reverse('detail', args=[self.unique_key])

    def save(self, *args, **kwargs):
        if not self.id:
            self.generate_unique_key()
            self.generate_extension()
            self.generate_image_filename()

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

    def generate_image_filename(self):
        image_name = '%s%s' % (self.unique_key, self.extension)
        self.image.name = image_name

    def generate_thumbnails(self):
        name = '%s_s%s' % (self.unique_key, self.extension)
        small_thumb = create_thumb(self.image, (150, 150))
        self.thumb_small.save(name, small_thumb)

        name = '%s_l%s' % (self.unique_key, self.extension)
        large_thumb = create_thumb(self.image, (700, 700))
        self.thumb_large.save(name, large_thumb)
