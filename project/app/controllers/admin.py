from django.shortcuts import render
from ..models import Categories, Products

""" Helper Functions """

def prodsInCategories():
    products = Products.objects.all()
    countProdsInCats = {}
    
    for product in products:
        if product.category_id not in countProdsInCats:
            countProdsInCats[product.category_id] = 1
        else:
            countProdsInCats[product.category_id] += 1

    prodsInCats = []
    for cat in Categories.objects.all():
        prodsInCats.append({
            "label": cat.name,
            "y": countProdsInCats.get(cat.id, 0)
        })

    return prodsInCats

def peodsByRating():
    products = Products.objects.all()
    countProdsByRating = {}
    
    for product in products:
        if product.rating not in countProdsByRating:
            countProdsByRating[product.rating] = 1
        else:
            countProdsByRating[product.rating] += 1

    prodsByRating = []
    for rating in range(1, 6):
        prodsByRating.append({
            "label": rating,
            "y": countProdsByRating.get(rating, 0)
        })

    return prodsByRating

""" Controller Functions """

def crtAdminPanel(request):
    nProds = Products.objects.count()
    nProdsNoStock = Products.objects.filter(stock = 0).count()
    nCats = Categories.objects.count()
    prodsInCats = prodsInCategories()
    prodsByRating = peodsByRating()
    return render(request, "adminPanel.html", { "nProds": nProds, "nProdsNoStock": nProdsNoStock, "nCats": nCats, "prodsInCats": prodsInCats, "prodsByRating": prodsByRating })