from django.db import models

# Create your models here.
class UploadImage (models.Model):
    image = models.ImageField(upload_to="data/", blank=True, null=True)
    
    def __str__(self):
        return "Image"  

class EncryptionData (models.Model):
    userData = models.TextField()