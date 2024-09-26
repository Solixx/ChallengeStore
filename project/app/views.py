from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Categories, Products
from django.core import serializers

# Create your views here.
def home(request):
    return render(request, "home.html")

def products(request):
    products = Products.objects.all()
    return render(request, "products.html", { "products": products })

def adminPanel(request):
    nProds = Products.objects.count()
    nProdsNoStock = Products.objects.filter(stock = 0).count()
    nCats = Categories.objects.count()
    return render(request, "adminPanel.html", { "nProds": nProds, "nProdsNoStock": nProdsNoStock, "nCats": nCats })


""" PRODUCTS """

def adminListProducts(request):
    products = Products.objects.all().order_by('-created_at')
    categories = Categories.objects.all()
    return render(request, "adminProducts.html", { "products": products, "categories": categories })

def adminProductProfile(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()
    
    return render(request, "adminProductProfile.html", { "product": product, "categories": categories })

def adminProductEdit(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()

    if request.method == "POST":  
        name = request.POST.get("name")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        category_id = request.POST.get("category")

        if name:
            product.name = name

        if price:
            try:
                price = float(price)
                product.price = price
            except ValueError:
                return HttpResponse("Price must be a valid float", status=400)

        if stock:
            try:
                stock = int(stock)
                product.stock = stock
            except ValueError:
                return HttpResponse("Stock must be a valid integer", status=400)

        if category_id:
            try:
                category = Categories.objects.get(id=category_id)
                if not category.is_deleted:
                    product.category = category
                else:
                    return HttpResponse("Category is disabled", status=400)
            except Categories.DoesNotExist:
                return HttpResponse("Category does not exist", status=400)

        if request.FILES.get('image'):
            product.image = request.FILES['image']

        product.save()
        
        serializedProduct = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'stock': product.stock,
            'image_name': product.image.name if product.image else None,
            'image_url': product.image.url if product.image else None,
            'category_id': product.category.id if product.category else None,
            'category_name': product.category.name if product.category else None,
            'is_deleted': product.is_deleted
        }
        serializedCategories = serializers.serialize("json", categories)

        return JsonResponse({"success": True, "message": "Product updated successfully", "product": serializedProduct, "categories": serializedCategories})
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

def adminProductDelete(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()

    serializedProduct = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'stock': product.stock,
            'image_name': product.image.name if product.image else None,
            'image_url': product.image.url if product.image else None,
            'category_id': product.category.id if product.category else None,
            'category_name': product.category.name if product.category else None,
            'is_deleted': True
        }
    serializedCategories = serializers.serialize("json", categories)

    product = Products.objects.get(id=id)
    product.delete()

    return JsonResponse({"success": True, "message": "Product updated successfully", "product": serializedProduct, "categories": serializedCategories})

def adminProductRestore(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()

    serializedProduct = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'stock': product.stock,
            'image_name': product.image.name if product.image else None,
            'image_url': product.image.url if product.image else None,
            'category_id': product.category.id if product.category else None,
            'category_name': product.category.name if product.category else None,
            'is_deleted': False
        }
    serializedCategories = serializers.serialize("json", categories)

    product = Products.deleted_objects.get(id=id)
    product.restore()

    return JsonResponse({"success": True, "message": "Product updated successfully", "product": serializedProduct, "categories": serializedCategories})

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
    categories = Categories.objects.all()
    return render(request, "adminProducts.html", { "products": products, "categories": categories })


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