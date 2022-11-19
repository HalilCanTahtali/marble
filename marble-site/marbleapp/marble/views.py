from email.mime import image
from unicodedata import category
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from marble.models import Marble,Category
from sklearn.cluster import KMeans
import cv2, numpy as np
from . import color_analysis
from django.utils.text import slugify





# Create your views here.

def index(request):
    
    context = {
        "marbles": Marble.objects.filter(is_active=True,is_home=True).order_by("-id"),
        "categories": Category.objects.all()
    }
    
    return render(request,"marble/index.html",context)


def marbles(request):
    
    context = {
        "marbles":Marble.objects.filter(is_active=True).order_by("-id"),
        "categories": Category.objects.all()
    }
    
    return render(request,"marble/marbles.html",context)
   
def marbles_by_category(request,slug):
     
    context = {
        
        "marbles":Marble.objects.filter(is_active=True, category__slug=slug).order_by("-id"),
        "categories": Category.objects.all(),
        "category_name": Category.objects.get(slug=slug),
        "selected_category": slug,
       
        
        
       
    }
    return render(request,"marble/marbles.html",context)


def marble_details(request,slug):
       
    
    marble = Marble.objects.get(slug=slug)
    
    return render(request,"marble/marble-details.html",{
        "categories": Category.objects.all(),
        "marble" : marble,
       
        
        
        })
    
    