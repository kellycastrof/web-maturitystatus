from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .apps import FruitConfig
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import os
from pathlib import Path


types=["Immature", "Partially Mature", "Mature", "Over-mature"]


def analyze(image_path):
    try:
        model= os.path.join(settings.BASE_DIR,"model/modelMB.h5")
        weights= os.path.join(settings.BASE_DIR,"model/weightsMB.h5")
        modelMB=load_model(model)
        modelMB.load_weights(weights)
        x=load_img(image_path,target_size=(224,224))
        x=img_to_array(x)
        x=np.expand_dims(x,axis=0)
        x=x/255
        arr=modelMB.predict(x)
        result=arr[0]
        max_result= np.amax(result)
        if max_result < 0.1:
            return "None"
        response=np.argmax(result)
        return types[response]
    except Exception as error:
        print(error)
        return error


class Home(APIView):
    def get(self, request, format=None):   
        return render(request, 'clasificador/template.html')
    def post(self, request, format=None):
        image= request.FILES['file']
        if image:
            fileimg= FileSystemStorage()
            saved= fileimg.save(image.name, image)
            path = fileimg.path(saved)
            context={
                'img':image.name,
                'size':image.size,
                'type': str(image.content_type),
            }
            try:
                result = analyze(path)
                context['class']=result      
            except:
                context['error']= "Something went wrong, try later"
            finally:
                return render(request, 'result.html', context)
        else:
            return render(request, 'result.html')

def about_us(request):
    return render(request, 'aboutus.html')