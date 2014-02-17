from django import forms


class UploadForm(forms.Form):
    url = forms.URLField()
