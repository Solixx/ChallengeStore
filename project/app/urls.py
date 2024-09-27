from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    # AUTH
    path('register/', views.register, name='register'),
    # Admin Panel - Dashboard
    path('adminPanel/', views.adminPanel, name='adminPanel'), #Dashboard
    # Admin Panel - Products
    path('adminPanel/products/', views.adminListProducts, name='adminListProducts'), #Listar Produtos
    path('adminPanel/products/<int:id>/', views.adminProductProfile, name='adminProductProfile'), #Página Perfil do Produto
    path('adminPanel/products/delete/<int:id>/', views.adminProductDelete, name='adminProductDelete'), #Ação Remover Produto
    path('adminPanel/products/restore/<int:id>/', views.adminProductRestore, name='adminProductRestore'), #Ação Restore Produto
    path('adminPanel/products/edit/<int:id>/', views.adminProductEdit, name='adminProductEdit'), #Página Editar Produto
    path('adminPanel/products/new/', views.adminPageProductNew, name='adminPageProductNew'), #Página Novo Produto
    path('adminPanel/products/create/', views.adminProductCreate, name='adminProductCreate'), #Ação Criar Produto
    # Admin Panel - Categories
    path('adminPanel/categories/', views.adminListCategories, name='adminListCategories'), #Lista Categorias
    path('adminPanel/categories/<int:id>/', views.adminCategoryProfile, name='adminCategoryProfile'),
    path('adminPanel/categories/delete/<int:id>/', views.adminCategoryDelete, name='adminCategoryDelete'),
    path('adminPanel/categories/restore/<int:id>/', views.adminCategoryRestore, name='adminCategoryRestore'),
    path('adminPanel/categories/edit/<int:id>/', views.adminCategoryEdit, name='adminCategoryEdit'),
    path('adminPanel/categories/new/', views.adminPageCategoriesNew, name='adminPageCategoriesNew'),
    path('adminPanel/categories/create/', views.adminCategoryCreate, name='adminCategoryCreate'),
]