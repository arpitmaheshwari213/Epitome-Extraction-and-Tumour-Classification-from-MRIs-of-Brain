from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from lib.test import *
import os
from lib.show_images import save_image_as_jpeg
# Create your views here.
def index(request):
    template = loader.get_template('brain_cancer/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def result(request):
    template = loader.get_template('brain_cancer/result.html')
    context = {}
    return HttpResponse(template.render(context, request))


def process(request):
    if request.method == 'POST' and request.FILES.get('input_image'):
        myfile = request.FILES.get('input_image')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        path_img=os.getcwd()+uploaded_file_url
        save_image_as_jpeg(path_img)
        if output(path_img) == 0:
            str1 = 'Benign'
        else:
            str1 = 'Malignant'
        return render(request, 'brain_cancer/result.html/', {'str': str1, 'uploaded_file_url': uploaded_file_url})
    return render(request, 'brain_cancer/result.html')
