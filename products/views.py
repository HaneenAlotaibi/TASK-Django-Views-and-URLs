
import string
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def get_home(request):
    prodect=Product.objects.get(id=1)
    return HttpResponse(f"<h1>Welcom {prodect.name}</h1>")

def get_product(request,Prodect_id):
    prodect=Product.objects.get(id=Prodect_id)
    string1=(f'name: {prodect.name}' 
    f' price: {prodect.price} '
    f'description: {prodect.description}')
    return HttpResponse(string1)    