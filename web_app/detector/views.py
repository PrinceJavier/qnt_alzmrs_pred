from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from django.http import HttpResponseRedirect
from django.urls import reverse

#-----------------------------

from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render  
from detector.forms import UserImageForm  
from .models import UploadImage  
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'detector/test.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'detector/test.html', {'form': form})