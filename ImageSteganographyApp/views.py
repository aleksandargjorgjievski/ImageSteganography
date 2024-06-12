from django.shortcuts import render
from .models import UploadImage
from .forms import UploadImageForm
# Create your views here.
def index(request):
    image = UploadImage.objects.first()
    
    if request.method == "POST":
    
        upload_image_form = UploadImageForm(request.POST, files = request.FILES)
        
        if upload_image_form.is_valid():
            if image:
                image.delete()
            
            upload_image = upload_image_form.save(commit=False)
            upload_image.image = upload_image_form.cleaned_data['image']
            upload_image.save()
            
            image = upload_image
    else:
        upload_image_form = UploadImageForm()
    
    return render(request, "index.html", {"image": image, "form": UploadImageForm})