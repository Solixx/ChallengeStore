from django.db import models
from django import forms

# Managers

class ActiveClassManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False) # This will return only the class content that are not deleted
    
class AllClassManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all() # This will return all the class content
    
class DeletedClassManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True) # This will return only the class content  that are deleted

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255)

    # Soft delete field
    is_deleted = models.BooleanField(default=False)

    objects = AllClassManager()  # All categories 
    deleted_objects = DeletedClassManager() # Only soft-deleted categories
    active_objects = ActiveClassManager() # Active categories (not deleted)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        products = Products.objects.filter(category_id = self.id)
        for product in products:
            product.delete()
        self.save()

    def hard_delete(self, *args, **kwargs):
        # Call the real delete method to permanently delete the object
        products = Products.objects.filter(category_id=self.id)
        for product in products:
            product.hard_delete() 

        super(Products, self).delete(*args, **kwargs)

    def restore(self):
        self.is_deleted = False
        self.save()

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # Soft delete field
    is_deleted = models.BooleanField(default=False)

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')

    objects = AllClassManager() # All products
    deleted_objects = DeletedClassManager() # Only soft-deleted products
    active_objects = ActiveClassManager() # Active products (not deleted)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        # Call the real delete method to permanently delete the object
        super(Products, self).delete(*args, **kwargs)

    def restore(self):
        category = Categories.objects.get(id=self.category_id)
        if not category.is_deleted:
            self.is_deleted = False
            self.save()
        