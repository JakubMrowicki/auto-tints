from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'friendly_name',
        'name'
    ]
    ordering = ('name',)


# class ProductAdmin(admin.ModelAdmin):


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
