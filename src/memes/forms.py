import re
from cStringIO import StringIO
from django import forms
from django.core.files.images import ImageFile

from images.models import Image


class MemeUploadForm(forms.Form):
    source_image = forms.ModelChoiceField(Image.objects.all())
    file = forms.CharField()
    mime = forms.CharField()
    top_text = forms.CharField()
    bottom_text = forms.CharField()

    def clean_file(self):
        data = self.cleaned_data['file']
        matches = re.search(r'base64,(.*)', data)
        imgstr = matches.group(1)
        imgcontent = StringIO(imgstr.decode('base64'))
        img = ImageFile(imgcontent, name='temp.png')

        return img
