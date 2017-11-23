from django.shortcuts import render

from .models import UploadedImage


def index(request):
    context = {'images': UploadedImage.objects.all()}
    return render(request, 'images/index.html', context)
