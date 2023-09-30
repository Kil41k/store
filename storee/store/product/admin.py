from django.contrib import admin
from product.models import ProductCategories, Products, Basket

admin.site.register(ProductCategories)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'descriptoin', ('price', 'quantity'), 'img', 'category')
    search_fields = ('name',)
    ordering = ('name',)

