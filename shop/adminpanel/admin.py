from django.contrib import admin
from .models import Shop, Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
