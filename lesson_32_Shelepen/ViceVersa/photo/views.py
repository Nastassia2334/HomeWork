from django.shortcuts import render
from .models import Photo

# Create your views here.
def photo(request):
    photos = Photo.objects.all()
    context = {
        "photos": photos,
    }
    return render(request, "photo_add.html", context)