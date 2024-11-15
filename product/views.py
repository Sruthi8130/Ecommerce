from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import *

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    pr=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        pr=product.objects.filter(category=c_page,available=True)
    else:
        pr=product.objects.all().filter(available=True)


    ct=categ.objects.all()
    
    return render(request,'index.html',{'pr':pr,'ct':ct})

def proddetails(request,c_slug,product_slug):
    try:
        pr=product.objects.get(category__slug=c_slug,slug=product_slug)
    
    except Exception as r:
        raise r
    return render(request,'about.html',{'pr':pr})

def mainpage(request):
     return render(request,'mainpage.html')




