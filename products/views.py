from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def get_home(request):
    return HttpResponse("<h1>Welcome</h1>")


def get_product(request, Prodect_id):
    prodect = Product.objects.get(id=Prodect_id)
    # string1=(f'name: {prodect.name}'
    # f' price: {prodect.price} '
    # f'description: {prodect.description}')
    return HttpResponse(
        f"<p> name: {prodect.name} </p><p>price: {prodect.price} </p> <p> description: {prodect.description}</p>"
    )


def get_products(request, Prodect_id):
    prodects = Product.objects.get(id=Prodect_id)
    new_products = []

    new_products.append(
        {
            "name": prodects.name,
            "price": prodects.price,
            "description": prodects.description,
        }
    )
    context = {"prodects": new_products}
    return render(request, "product_detail.html", context)


def get_productss(request):
    prodects = Product.objects.all()
    new_products = []
    for prodect in prodects:
        new_products.append(
            {
                "name": prodect.name,
                "price": prodect.price,
                "description": prodect.description,
            }
        )
    context = {"prodects": new_products}
    return render(request, "product-list.html", context)
