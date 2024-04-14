from django.contrib import admin
from .models import Product, Review

# Register your models here.

@admin.register(Product)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'reting', 'is_available', 'price', 'discount', 'stock', )
    list_editable = ('price', 'stock')

@admin.register(Review)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('autor', 'product', 'like', 'dislike', )