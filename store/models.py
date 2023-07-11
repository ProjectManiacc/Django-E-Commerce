from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    
    def discount(self):
        return round(self.price - (self.price * 0.2))
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
