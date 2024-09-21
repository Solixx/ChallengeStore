from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def home(request):
    return render(request, "home.html")

def products(request):
    products = Products.objects.all()
    return render(request, "products.html", { "products": products })