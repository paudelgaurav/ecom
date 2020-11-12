from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.


def productDetailView(request,category_slug,slug):

    product = get_object_or_404(Product,slug=slug)

    return render(request,'store/detail.html',{'product':product})