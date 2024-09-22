from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Products

# Create your views here.
def home(request):
    return render(request, "home.html")

def products(request):
    products = Products.objects.all()
    return render(request, "products.html", { "products": products })

def adminPanel(request):
    products = Products.objects.all()
    return render(request, "adminPanel.html", { "products": products })

def adminProductProfile(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, "productAdminProfile.html", { "product": product })

def adminProductEdit(request, id):
    product = get_object_or_404(Products, id=id)

    if request.method == "POST":
        product = Products.objects.get(id=id)
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.stock = request.POST["stock"]
        product.save()

        return redirect('adminPanel')
    
    products = Products.objects.all()
    return render(request, "adminPanel.html", {"products": products})

def adminProductDelete(request, id):
    get_object_or_404(Products, id=id)

    Products.objects.get(id=id).delete()
    return redirect('adminPanel')