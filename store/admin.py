from django.contrib import admin
from .models import Category, Pet, Product

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'price', 'is_available')
    list_filter = ('species', 'is_available')
    search_fields = ('name', 'species', 'breed')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'category__name')

admin.site.register(Category)
admin.site.register(Pet, PetAdmin)
admin.site.register(Product, ProductAdmin)
