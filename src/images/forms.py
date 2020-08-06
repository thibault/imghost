from django import forms


class UploadForm(forms.Form):
    url = forms.URLField(required=False)
    file = forms.FileField(required=False)

    def clean(self):
        data = super(UploadForm, self).clean()

        values = list(data.values()) + list(self.files.values())
        if not any(values) or all(values):
            raise forms.ValidationError('Upload a file or give a url')

        return data
