from django.contrib import admin
from .models import UploadImage, EncryptionData, DecryptedImage

# Register your models here.
admin.site.register(UploadImage)
admin.site.register(EncryptionData)
admin.site.register(DecryptedImage)