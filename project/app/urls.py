from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('adminPanel/', views.adminPanel, name='adminPanel'),
    path('adminPanel/product/<int:id>/', views.adminProductProfile, name='productAdminProfile'),
]