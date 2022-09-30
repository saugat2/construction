from multiprocessing import context
from tkinter import Variable
from django.shortcuts import render,HttpResponse
from .models import Blog,Gallery_image
from math import ceil


# Create your views here.
def index(request):
    gallery=Gallery_image.objects.all()
    blog_index=Blog.objects.all()
    print(gallery)
    n= len(gallery)
    nSlides=n//4 +ceil((n/4)-(n//4))
    params={'no_of_slides':nSlides,'range':range(nSlides) ,'image':gallery,'blog':blog_index}
    return render(request,'index.html',params)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'aboutus.html')

def project(request):
    return render(request,'goingproject.html')

def blog_desc(request,id):
    blogs=Blog.objects.filter(id = id).first()
    context={'blogs':blogs}
    return render(request,'blogdetail.html',context)
    