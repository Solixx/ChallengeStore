from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from ..models import Categories, Products
from django.core.paginator import Paginator

""" Helper Functions """

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

        if price:
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
            elif price == "-1":
                price = ""

        if stock:
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
            elif stock == "-1":
                stock = ""

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
            "category": 0
        }
        products = products.filter(category_id = haveCategory[1])

    return {"searchObj": searchObj, "products": products}



""" Controller Functions """

def crtAdminListCategories(request):
    search = ""

    if request.method == "POST":
        search = request.POST.get("search")

        if search:
            categories = Categories.objects.filter(name__icontains = search).order_by('-created_at')
        else:
            categories = Categories.objects.all().order_by('-created_at')
    else:
        categories = Categories.objects.all().order_by('-created_at')

    paginator = Paginator(categories, 3)

    if search == "":
        if request.method == "GET":
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, "adminCategories.html", { "categories": page_obj, "search": search })
        else:
            page_number = 1
            page_obj = paginator.get_page(page_number)

            return render(request, "adminCategories.html", { "categories": page_obj, "search": search })
        
    return render(request, "adminCategories.html", { "categories": categories, "search": search })


def crtAdminPageCategoriesNew(request):
    return render(request, "adminCategoryNew.html")


def crtAdminCategoryCreate(request):
    if request.method == "POST":
        category = Categories()
        category.name = request.POST["name"]
        category.save()

        return render(request, "adminCategoryProfile.html", { "category": category })
    
    categories = Categories.objects.all()
    return render(request, "adminCategories.html", { "categories": categories })


def crtAdminCategoryProfile(request, id):
    category = get_object_or_404(Categories, id=id)
    categories = Categories.objects.all()

    searchObj = {
        "search": "",
        "price": "",
        "stock": "",
        "category": 0
    }

    searchObj = searchProductsForm(request, [False, id])['searchObj']
    products = searchProductsForm(request, [False, id])['products']  

    paginator = Paginator(products, 3)

    if searchObj["search"] == "" and searchObj["price"] == "" and searchObj["stock"] == "" and searchObj["category"] == 0:
        if request.method == "GET":
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, "adminCategoryProfile.html", { "category": category, "products": page_obj, "categories": categories, "searchObj": searchObj })
        else:
            page_number = 1
            page_obj = paginator.get_page(page_number)

            return render(request, "adminCategoryProfile.html", { "category": category, "products": page_obj, "categories": categories, "searchObj": searchObj })

    return render(request, "adminCategoryProfile.html", { "category": category, "products": products, "categories": categories, "searchObj": searchObj })


def crtAdminCategoryEdit(request, id):
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


def crtAdminCategoryDelete(request, id):
    category = get_object_or_404(Categories, id=id)
    category.delete()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)


def crtAdminCategoryRestore(request, id):
    category = get_object_or_404(Categories, id=id)
    category.restore()

    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)