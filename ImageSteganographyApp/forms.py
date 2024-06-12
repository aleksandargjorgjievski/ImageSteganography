from django import forms

from .models import UploadImage, EncryptionData

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

class EncryptionDataForm (forms.ModelForm):
    class Meta:
        model = EncryptionData
        fields = ["userData",]
        widgets = {
            'userData': forms.TextInput(attrs={'required': True})
        }
    def __init__(self, *args, **kwargs):
        super(EncryptionDataForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'