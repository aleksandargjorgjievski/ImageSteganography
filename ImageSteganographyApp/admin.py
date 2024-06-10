from django.contrib import admin
from .models import UploadImage, EncryptionData

# Register your models here.
admin.site.register(UploadImage)
admin.site.register(EncryptionData)