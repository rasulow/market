from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Kategoriýa'
        verbose_name_plural = 'Kategoriýalar'
        
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    UNIT_CHOICES = [
        ('kg', 'kilogram'),
        ('piece', 'ştuk')
    ]
    
    name = models.CharField(max_length=50)
    short_description = models.TextField(null=True)
    price = models.FloatField()
    unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
    count_in_stock = models.IntegerField()
    total_price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Haryt'
        verbose_name_plural = 'Harytlar'
    
    def save(self, *args, **kwargs):
        self.total_price = float(self.price) * float(self.count_in_stock)
        
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.name
    
    
class Bill(models.Model):
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'bill'
        verbose_name = 'Çek'
        verbose_name = 'Çekler'

    def __str__(self) -> str:
        return str(self.id)
    
    
class BillProducts(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.FloatField()
    total_price = models.FloatField()
    
    class Meta:
        db_table = 'bill_products'
        verbose_name = 'Çek element'
        verbose_name_plural = 'Çek elementleri'
        
    def __str__(self) -> str:
        return str(self.bill.id)