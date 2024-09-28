from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Categories, Products
from django.core import serializers
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def searchProductsForm(request, haveCategory):
    products = Products.objects.all().order_by('-created_at')
    search = ""
    price = ""
    stock = ""
    category = 0

    if request.method == "POST":
        search = request.POST.get("search")
        price = request.POST.get("searchPrice")
        stock = request.POST.get("searchStock")
        category = request.POST.get("searchCategory")

        if search:
            products = Products.objects.filter(name__icontains = search).order_by('-created_at')

        if price and price != "-1":
            if price == "0":
                products = products.filter(price = 0).order_by('-created_at')
            elif price == "100":
                products = products.filter(price__lt = 100).filter(price__gt = 0).order_by('-created_at')
            elif price == "250":
                products = products.filter(price__lt = 250).filter(price__gt = 100).order_by('-created_at')
            elif price == "500":
                products = products.filter(price__lt = 500).filter(price__gt = 250).order_by('-created_at')
            elif price == "500+":
                products = products.filter(price__gte = 500).order_by('-created_at')

        if stock and stock != "-1":
            if stock == "0":
                products = products.filter(stock = 0).order_by('-created_at')
            elif stock == "25":
                products = products.filter(stock__lt = 25).filter(stock__gt = 0).order_by('-created_at')
            elif stock == "50":
                products = products.filter(stock__lt = 50).filter(stock__gt = 25).order_by('-created_at')
            elif stock == "100":
                products = products.filter(stock__lt = 100).filter(stock__gt = 50).order_by('-created_at')
            elif stock == "100+":
                products = products.filter(stock__gte = 100).order_by('-created_at')

        if haveCategory[0] and category and Categories.objects.filter(id=int(category)).exists():
                products = products.filter(category_id = category).order_by('-created_at')
        
    if haveCategory[0]:
        searchObj = {
            "search": search,
            "price": price,
            "stock": stock,
            "category": int(category)
        }
    else:
        searchObj = {
            "search": search,
            "price": price,
            "stock": stock,
        }
        products = products.filter(category_id = haveCategory[1])

    return {"searchObj": searchObj, "products": products}

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def adminPanel(request):
    nProds = Products.objects.count()
    nProdsNoStock = Products.objects.filter(stock = 0).count()
    nCats = Categories.objects.count()
    return render(request, "adminPanel.html", { "nProds": nProds, "nProdsNoStock": nProdsNoStock, "nCats": nCats })


""" PRODUCTS """

@login_required
def adminListProducts(request):
    categories = Categories.objects.all()
    
    searchObj = searchProductsForm(request, [True, "0"])['searchObj']
    products = searchProductsForm(request, [True, "0"])['products']

    return render(request, "adminProducts.html", { "products": products, "categories": categories, "searchObj": searchObj })

@login_required
def adminProductProfile(request, id):
    product = get_object_or_404(Products, id=id)
    categories = Categories.objects.all()
    
    return render(request, "adminProductProfile.html", { "product": product, "categories": categories })

@login_required
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

@login_required
def adminProductDelete(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)

@login_required
def adminProductRestore(request, id):
    product = get_object_or_404(Products, id=id)
    product.restore()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)

@login_required
def adminPageProductNew(request):
    categories = Categories.objects.all()
    return render(request, "adminProductNew.html", { "categories": categories })

@login_required
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

@login_required
def adminListCategories(request):
    search = ""

    if request.method == "POST":
        search = request.POST.get("search")

        if search:
            categories = Categories.objects.filter(name__icontains = search).order_by('-created_at')
        else:
            categories = Categories.objects.all().order_by('-created_at')
    else:
        categories = Categories.objects.all().order_by('-created_at')

    return render(request, "adminCategories.html", { "categories": categories, "search": search })

@login_required
def adminPageCategoriesNew(request):
    return render(request, "adminCategoryNew.html")

@login_required
def adminCategoryCreate(request):
    if request.method == "POST":
        category = Categories()
        category.name = request.POST["name"]
        category.save()

        return render(request, "adminCategoryProfile.html", { "category": category, "products": products })
    
    categories = Categories.objects.all()
    return render(request, "adminCategories.html", { "categories": categories })

@login_required
def adminCategoryProfile(request, id):
    category = get_object_or_404(Categories, id=id)
    categories = Categories.objects.all()

    searchObj = searchProductsForm(request, [False, id])['searchObj']
    products = searchProductsForm(request, [False, id])['products']  
    
    return render(request, "adminCategoryProfile.html", { "category": category, "products": products, "categories": categories, "searchObj": searchObj })

@login_required
def adminCategoryEdit(request, id):
    category = get_object_or_404(Categories, id=id)

    if request.method == "POST":
        category = Categories.objects.get(id=id)
        category.name = request.POST["name"]
        category.save()

        serializedCategory = {
            'id': category.id,
            'name': category.name,
            'is_deleted': category.is_deleted,
            'created_at': category.created_at,
            'updated_at': category.updated_at
        }

        return JsonResponse({"success": True, "message": "Product updated successfully", "category": serializedCategory})
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

@login_required
def adminCategoryDelete(request, id):
    category = get_object_or_404(Categories, id=id)
    category.delete()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)

@login_required
def adminCategoryRestore(request, id):
    category = get_object_or_404(Categories, id=id)
    category.restore()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)



""" AUTH """

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})