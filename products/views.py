from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
def get_home(request):
    return HttpResponse("<h1>Welcome</h1>")

def get_product(request,Prodect_id):
    prodect=Product.objects.get(id=Prodect_id)
    # string1=(f'name: {prodect.name}' 
    # f' price: {prodect.price} '
    # f'description: {prodect.description}')
    return HttpResponse(f"<p> name: {prodect.name} </p><p>price: {prodect.price} </p> <p> description: {prodect.description}</p>")    