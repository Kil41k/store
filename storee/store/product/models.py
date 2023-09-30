from django.db import models
import os
from users.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

class ProductCategories(models.Model):
    name = models.CharField(max_length=128)
    descriptoin = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    def __str__(self):
        return self.name
class Products(models.Model):
    name = models.CharField(max_length=256)
    descriptoin = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='ProductsImages')
    category = models.ForeignKey(to=ProductCategories, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
    def __str__(self):
        return self.name
    
class basketQRS(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    def total_quantity(self):
        return sum(basket.quantity for basket in self)
    
class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_timetamp = models.DateTimeField(auto_now_add=True)
    objects = basketQRS.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity
    
