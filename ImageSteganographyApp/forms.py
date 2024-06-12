from django import forms

from .models import UploadImage

class UploadImageForm (forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ["image",]
        widgets = {
            'image': forms.FileInput(attrs={'required': True})
        }
    def __init__(self, *args, **kwargs):
        super(UploadImageForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'