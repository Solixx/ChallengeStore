from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    # Admin Panel - Products
    path('adminPanel/', views.adminPanel, name='adminPanel'), #Dashboard
    path('adminPanel/product/<int:id>/', views.adminProductProfile, name='productAdminProfile'), #Página Perfil do Produto
    path('adminPanel/product/delete/<int:id>/', views.adminProductDelete, name='productAdminDelete'), #Ação Remover Produto
    path('adminPanel/product/restore/<int:id>/', views.adminProductRestore, name='productAdminRestore'), #Ação Restore Produto
    path('adminPanel/product/edit/<int:id>/', views.adminProductEdit, name='productAdminEdit'), #Página Editar Produto
    path('adminPanel/product/new/', views.productAdminNewProductPage, name='productAdminNewProductPage'), #Página Novo Produto
    path('adminPanel/product/create/', views.adminProductCreate, name='adminProductCreate'), #Ação Criar Produto
    # Admin Panel - Categories
    path('adminPanel/categories/', views.adminPanelCategories, name='adminPanelCategories'), #Lista Categorias
    path('adminPanel/categories/<int:id>/', views.adminCategoryProfile, name='categoriesAdminProfile'),
    path('adminPanel/categories/delete/<int:id>/', views.adminCategoryDelete, name='adminCategoryDelete'),
    path('adminPanel/categories/restore/<int:id>/', views.adminCategoryRestore, name='adminCategoryRestore'),
    path('adminPanel/categories/edit/<int:id>/', views.adminCategoryEdit, name='adminCategoryEdit'),
    path('adminPanel/categories/new/', views.categoriesAdminNewCategoryPage, name='categoriesAdminNewCategoryPage'),
    path('adminPanel/categories/create/', views.adminCategoryCreate, name='adminCategoryCreate'),
]