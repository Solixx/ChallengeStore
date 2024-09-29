from django.shortcuts import render
from ..models import Categories, Products

def crtAdminPanel(request):
    nProds = Products.objects.count()
    nProdsNoStock = Products.objects.filter(stock = 0).count()
    nCats = Categories.objects.count()
    return render(request, "adminPanel.html", { "nProds": nProds, "nProdsNoStock": nProdsNoStock, "nCats": nCats })