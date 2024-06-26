from django import forms

from .models import UploadImage, EncryptionData, DecryptedImage

class UploadImageForm (forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ["image",]
        widgets = {
            'image': forms.FileInput(attrs={'required': True})
        }
        labels = {
            'image': "Image to be encoded",
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
            'userData': forms.Textarea(attrs={
                'required': True,
                'placeholder': "Enter text...",
                'style': 'width: 20vw; height: 40vh; resize: none; padding: 0; text-align: left;',
                }),
        }
        labels = {
            'userData': "Text to be encoded:",
        }
    def __init__(self, *args, **kwargs):
        super(EncryptionDataForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class DecryptionImageForm (forms.ModelForm):
    class Meta:
        model = DecryptedImage
        fields = ["image",]
        widgets = {
            'image': forms.FileInput(attrs={'required': True})
        }
        labels = {
            'image': "Image to be decoded",
        }
    def __init__(self, *args, **kwargs):
        super(DecryptionImageForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'