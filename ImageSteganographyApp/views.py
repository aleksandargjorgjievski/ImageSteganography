from django.shortcuts import render
from .models import UploadImage
# Create your views here.
def index(request):
    images = UploadImage.objects.all()
    
    return render(request, "index.html", {"images": images})