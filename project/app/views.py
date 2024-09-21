from django.shortcuts import render, get_object_or_404
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
    """ products = Products.objects.get(id) """
    product = get_object_or_404(Products, id=id)
    return render(request, "productAdminProfile.html", { "product": product })