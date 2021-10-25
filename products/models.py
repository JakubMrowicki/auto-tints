"""
Models for the products app.
"""
from django.db import models


class Category(models.Model):
    """ Model for Categories """
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    image = models.ImageField(default="noimage.jpg")

    def __str__(self):
        """ return category name """
        return str(self.name)

    def get_friendly_name(self):
        """ return category friendly name """
        return self.friendly_name

    class Meta():
        verbose_name_plural = "Categories"


class Product(models.Model):
    """ Model for Products """
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default="noimage.jpg")

    def __str__(self):
        """ return product name """
        return str(self.name)
