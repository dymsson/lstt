import os
from django.db import models
from django.conf import settings

# Create your models here.

class Shop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    imageUrl = models.ImageField(upload_to='images/shop', null=True)

    def __str__(self):
         return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
         return self.title

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
    categories = models.ManyToManyField(Category)
    description = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    price = models.FloatField(default=100)
    active = models.BooleanField(default=True)

    def __str__(self):
         return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    images = models.ImageField(upload_to='images/product', null=True)

    def get_absolute_image_url(self):
        return os.path.join(settings.MEDIA_URL, self.images.url)
