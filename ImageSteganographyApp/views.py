from django.shortcuts import render
from .models import UploadImage, EncryptionData, DecryptedImage
from .forms import UploadImageForm, EncryptionDataForm, DecryptionImageForm
from .steganography import Encode, Decode
import os
# Create your views here.
def index(request):
    image = UploadImage.objects.first()
    text = EncryptionData.objects.first()

    message = None
    encoded_status = None

    if request.method == "POST":
            upload_image_form = UploadImageForm(request.POST, files = request.FILES)
            text_form = EncryptionDataForm(request.POST)
            if 'upload_image' in request.POST:
                if upload_image_form.is_valid():
                    if image:
                        image.delete()
                    
                    upload_image = upload_image_form.save(commit=False)
                    upload_image.image = upload_image_form.cleaned_data['image']
                    upload_image.save()
                    image = upload_image
            elif 'encode_text' in request.POST:
                 if text_form.is_valid():
                      if text:
                           text.delete()
                 uploaded_text = text_form.save(commit=False)
                 message = text_form.cleaned_data['userData']
                 if image:
                      src = image.image.path
                      dest_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'encoded')
                      filename, extension = os.path.splitext(os.path.basename(src))
                      dest = os.path.join(dest_folder, f"{filename}_encoded{extension}")
                      encoded_status = Encode(src, message, dest)
                 uploaded_text.save()
    else:
        upload_image_form = UploadImageForm()
        text_form = EncryptionDataForm()

    return render(request, "index.html", {"image": image, "upload_image_form": UploadImageForm, "text_form": EncryptionDataForm, "encoded_status": encoded_status})

def decode(request):
    decoded_image = DecryptedImage.objects.first()
    decoded_messsage = None

    if request.method == "POST":
        if 'upload_image' in request.POST:
            decrypted_image_form = DecryptionImageForm(request.POST, files = request.FILES)
            if decrypted_image_form.is_valid():
                if decoded_image:
                    decoded_image.delete()      
                upload_image = decrypted_image_form.save(commit=False)
                upload_image.image = decrypted_image_form.cleaned_data['image']
                upload_image.save()
                decoded_image = upload_image
        elif 'decode_text' in request.POST:
            if decoded_image:
                decoded_messsage = Decode(decoded_image.image.path)
    
    return render(request, "decode.html", {"image": decoded_image, "decrypted_image_form": DecryptionImageForm, "decoded_message": decoded_messsage})