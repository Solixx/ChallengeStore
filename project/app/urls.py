from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('adminPanel/', views.adminPanel, name='adminPanel'),
    path('adminPanel/product/<int:id>/', views.adminProductProfile, name='productAdminProfile'),
    path('adminPanel/product/delete/<int:id>/', views.adminProductDelete, name='productAdminDelete'),
    path('adminPanel/product/edit/<int:id>/', views.adminProductEdit, name='productAdminEdit'),
]