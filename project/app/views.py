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
    products = Products.objects.all()
    return render(request, "adminPanel.html", { "products": products })

def adminProductProfile(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()
    return render(request, "productAdminProfile.html", { "product": product, "categories": categories })

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

        return render(request, "productAdminProfile.html", { "product": product, "categories": categories })
    
    products = Products.objects.all()
    return render(request, "adminPanel.html", {"products": products})

def adminProductDelete(request, id):
    get_object_or_404(Products, id=id)

    Products.objects.get(id=id).delete()
    return redirect('adminPanel')

def adminProductRestore(request, id):
    get_object_or_404(Products, id=id)

    Products.deleted_objects.get(id=id).restore()
    return redirect('adminPanel')

def productAdminNewProductPage(request):
    categories = Categories.objects.all()
    return render(request, "productAdminNew.html", { "categories": categories })

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

        return render(request, "productAdminProfile.html", { "product": product, "categories": categories })
    
    products = Products.objects.all()
    return render(request, "adminPanel.html", {"products": products})

def adminPanelCategories(request):
    categories = Categories.objects.all()
    return render(request, "adminPanelCategories.html", { "categories": categories })

def categoriesAdminNewCategoryPage(request):
    return render(request, "categoryAdminNew.html")

def adminCategoryCreate(request):
    if request.method == "POST":
        category = Categories()
        category.name = request.POST["name"]
        category.save()

        return redirect('adminPanelCategories')
    
    categories = Categories.objects.all()
    return render(request, "adminPanelCategories.html", { "categories": categories })

def adminCategoryProfile(request, id):
    category = get_object_or_404(Categories, id=id)
    return render(request, "categoryAdminProfile.html", { "category": category })

def adminCategoryEdit(request, id):
    category = get_object_or_404(Categories, id=id)

    if request.method == "POST":
        category = Categories.objects.get(id=id)
        category.name = request.POST["name"]
        category.save()

        return render(request, "categoryAdminProfile.html", { "category": category })
    
    categories = Categories.objects.all()
    return render(request, "adminPanelCategories.html", {"categories": categories})

def adminCategoryDelete(request, id):
    get_object_or_404(Categories, id=id)

    Categories.objects.get(id=id).delete()
    return redirect('adminPanelCategories')

def adminCategoryRestore(request, id):
    get_object_or_404(Categories, id=id)

    Categories.deleted_objects.get(id=id).restore()
    return redirect('adminPanelCategories')