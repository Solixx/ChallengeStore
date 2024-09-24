from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categories, Products

# Create your views here.
def home(request):
    return render(request, "home.html")

def products(request):
    products = Products.objects.all()
    return render(request, "products.html", { "products": products })

def adminPanel(request):
    return render(request, "adminPanel.html")


""" PRODUCTS """

def adminListProducts(request):
    products = Products.objects.all().order_by('-created_at')
    return render(request, "adminProducts.html", { "products": products })

def adminProductProfile(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()
    return render(request, "adminProductProfile.html", { "product": product, "categories": categories })

def adminProductEdit(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()

    if request.method == "POST":
        product = Products.objects.get(id=id)
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.stock = request.POST["stock"]

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        category = Categories.objects.get(id = request.POST["category"])
        if not category.is_deleted:
            product.category = Categories.active_objects.get(id = request.POST["category"])
        else:
            return HttpResponse("Category does not exist")

        product.save()

        return render(request, "adminProductProfile.html", { "product": product, "categories": categories })
    
    products = Products.objects.all()
    return render(request, "adminProducts.html", {"products": products})

def adminProductDelete(request, id):
    get_object_or_404(Products, id=id)

    product = Products.objects.get(id=id)
    product.delete()
    categories = Categories.objects.all()
    return render(request, "adminProductProfile.html", { "product": product, "categories": categories })

def adminProductRestore(request, id):
    get_object_or_404(Products, id=id)

    product = Products.deleted_objects.get(id=id)
    product.restore()
    categories = Categories.objects.all()
    return render(request, "adminProductProfile.html", { "product": product, "categories": categories })

def adminPageProductNew(request):
    categories = Categories.objects.all()
    return render(request, "adminProductNew.html", { "categories": categories })

def adminProductCreate(request):
    categories = Categories.objects.all()
    if request.method == "POST":
        product = Products()
        product.name = request.POST["name"]
        product.price = request.POST["price"]
        product.stock = request.POST["stock"]

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        category = Categories.objects.get(id = request.POST["category"])
        if not category.is_deleted:
            product.category = Categories.active_objects.get(id = request.POST["category"])
        else:
            return HttpResponse("Category is deleted")

        product.save()

        return render(request, "adminProductProfile.html", { "product": product, "categories": categories })
    
    products = Products.objects.all()
    return render(request, "adminProducts.html", {"products": products})


""" CATEGORIES """

def adminListCategories(request):
    categories = Categories.objects.all().order_by('-created_at')
    return render(request, "adminCategories.html", { "categories": categories })

def adminPageCategoriesNew(request):
    return render(request, "adminCategoryNew.html")

def adminCategoryCreate(request):
    if request.method == "POST":
        category = Categories()
        category.name = request.POST["name"]
        category.save()

        return render(request, "adminCategoryProfile.html", { "category": category, "products": products })
    
    categories = Categories.objects.all()
    return render(request, "adminCategories.html", { "categories": categories })

def adminCategoryProfile(request, id):
    category = get_object_or_404(Categories, id=id)
    products = Products.objects.filter(category_id = id)
    return render(request, "adminCategoryProfile.html", { "category": category, "products": products })

def adminCategoryEdit(request, id):
    category = get_object_or_404(Categories, id=id)

    if request.method == "POST":
        category = Categories.objects.get(id=id)
        category.name = request.POST["name"]
        category.save()

        products = Products.objects.filter(category_id = id)

        return render(request, "adminCategoryProfile.html", { "category": category, "products": products })
    
    categories = Categories.objects.all()
    return render(request, "adminCategories.html", {"categories": categories})

def adminCategoryDelete(request, id):
    get_object_or_404(Categories, id=id)

    category = Categories.objects.get(id=id)
    category.delete()
    products = Products.objects.filter(category_id = id)
    return render(request, "adminCategoryProfile.html", { "category": category, "products": products })

def adminCategoryRestore(request, id):
    get_object_or_404(Categories, id=id)

    category = Categories.deleted_objects.get(id=id)
    category.restore()
    products = Products.objects.filter(category_id = id)
    return render(request, "adminCategoryProfile.html", { "category": category, "products": products })