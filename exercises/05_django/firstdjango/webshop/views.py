from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Product

def starting_instructions(request):
    return render(request, "webshop/instructions.html", {})

def about(request):
    return HttpResponse("about page")

def productview(request, product_id):
    produkttn = get_object_or_404(Product, pk = product_id)
    return render(request, "webshop/product_view.html", {'product' : produkttn})
    
def available_products(request):
    available = Product.objects.all().filter(quantity__gt=0)
    return render(request, "webshop/product_list.html", {'products' : available})