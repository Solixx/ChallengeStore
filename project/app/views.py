from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.decorators import staff_required
from .controllers.products import crtAdminListProducts, crtAdminProductProfile, crtAdminProductEdit, crtAdminProductDelete, crtAdminProductRestore, crtAdminPageProductNew, crtAdminProductCreate
from .controllers.categories import crtAdminListCategories, crtAdminPageCategoriesNew, crtAdminCategoryCreate, crtAdminCategoryProfile, crtAdminCategoryEdit, crtAdminCategoryDelete, crtAdminCategoryRestore
from .controllers.users import crtRegister
from .controllers.admin import crtAdminPanel


# Create your views here.
def home(request):
    return render(request, "home.html")

""" Admin Panel """

@login_required
@staff_required
def adminPanel(request):
    return crtAdminPanel(request)


""" PRODUCTS """

@login_required
@staff_required
def adminListProducts(request):
    return crtAdminListProducts(request)

@login_required
@staff_required
def adminProductProfile(request, id):
    return crtAdminProductProfile(request, id)

@login_required
@staff_required
def adminProductEdit(request, id):
    return crtAdminProductEdit(request, id)

@login_required
@staff_required
def adminProductDelete(request, id):
    return crtAdminProductDelete(request, id)

@login_required
@staff_required
def adminProductRestore(request, id):
    return crtAdminProductRestore(request, id)

@login_required
@staff_required
def adminPageProductNew(request):
    return crtAdminPageProductNew(request)
    
@login_required
@staff_required
def adminProductCreate(request):
    return crtAdminProductCreate(request)



""" CATEGORIES """

@staff_required
@login_required
def adminListCategories(request):
    return crtAdminListCategories(request)

@staff_required
@login_required
def adminPageCategoriesNew(request):
    return crtAdminPageCategoriesNew(request)

@staff_required
@login_required
def adminCategoryCreate(request):
    return crtAdminCategoryCreate(request)

@staff_required
@login_required
def adminCategoryProfile(request, id):
    return crtAdminCategoryProfile(request, id)
    
@staff_required
@login_required
def adminCategoryEdit(request, id):
    return crtAdminCategoryEdit(request, id)

@staff_required
@login_required
def adminCategoryDelete(request, id):
    return crtAdminCategoryDelete(request, id)

@staff_required
@login_required
def adminCategoryRestore(request, id):
    return crtAdminCategoryRestore(request, id)



""" AUTH """

def register(request):
    return crtRegister(request)