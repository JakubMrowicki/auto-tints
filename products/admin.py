from django.contrib import admin
from .models import Category, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'friendly_name',
        'name'
    ]
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price'
    ]
    ordering = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'product',
        'recommend',
        'date'
    ]
    ordering = ('date',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
