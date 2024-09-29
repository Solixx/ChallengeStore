from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # AUTH
    path('register/', views.register, name='register'),
    # Admin Panel - Dashboard
    path('adminPanel/', views.adminPanel, name='adminPanel'), #Dashboard
    # Admin Panel - Products
    path('adminPanel/products/', views.adminListProducts, name='adminListProducts'), #Listar Produtos
    path('adminPanel/product/<int:id>/', views.adminProductProfile, name='adminProductProfile'), #Página Perfil do Produto
    path('adminPanel/product/delete/<int:id>/', views.adminProductDelete, name='adminProductDelete'), #Ação Remover Produto
    path('adminPanel/product/restore/<int:id>/', views.adminProductRestore, name='adminProductRestore'), #Ação Restore Produto
    path('adminPanel/product/edit/<int:id>/', views.adminProductEdit, name='adminProductEdit'), #Página Editar Produto
    path('adminPanel/product/new/', views.adminPageProductNew, name='adminPageProductNew'), #Página Novo Produto
    path('adminPanel/product/create/', views.adminProductCreate, name='adminProductCreate'), #Ação Criar Produto
    # Admin Panel - Categories
    path('adminPanel/categories/', views.adminListCategories, name='adminListCategories'), #Lista Categorias
    path('adminPanel/categorie/<int:id>/', views.adminCategoryProfile, name='adminCategoryProfile'),
    path('adminPanel/categorie/delete/<int:id>/', views.adminCategoryDelete, name='adminCategoryDelete'),
    path('adminPanel/categorie/restore/<int:id>/', views.adminCategoryRestore, name='adminCategoryRestore'),
    path('adminPanel/categorie/edit/<int:id>/', views.adminCategoryEdit, name='adminCategoryEdit'),
    path('adminPanel/categorie/new/', views.adminPageCategoriesNew, name='adminPageCategoriesNew'),
    path('adminPanel/categorie/create/', views.adminCategoryCreate, name='adminCategoryCreate'),
]