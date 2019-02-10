import os
import json
import  requests
from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Slider,Category,Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    sliders = Slider.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    if request.method == 'GET':
        print(request.POST)
        #products = Product.objects.filter(price__lt = )
    context = {'sliders':sliders,'categories':categories,'products':products}
    return render(request,'webapp/index.html',context)
def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories':categories,'products':products}
    return render(request,'webapp/product.html',context)

def feature(request):
    return HttpResponse("<h1> Hello Feature</h1>")
def category(request,category_name,pk):
    categories = Category.objects.get(pk=pk)
    products = Product.objects.filter(category__id = pk )
    print(products)
    context = {'categories':categories,'products':products}
    return render(request,'webapp/category.html',context)

def products_detail(request,product_name,pk):
    product_detail = Product.objects.get(pk=pk)
    print(product_detail)
    context = {'product_detail':product_detail}
    return render(request,'webapp/product-detail.html',context)
def about(request):
    context ={}
    return render(request,'webapp/about.html',context)
def contact(request):
    context ={}
    return render(request,'webapp/contact.html',context)
