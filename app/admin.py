from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'unit', 'count_in_stock', 'total_price', 'category']
    list_filter = ['category']


class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price', 'formatted_created_at']

    def formatted_created_at(self, obj):
        # Format the created_at field as you desire
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
    
    formatted_created_at.short_description = 'Created At'  
    
    list_filter = ['created_at']
    
class BillProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill', 'product', 'count', 'total_price']
    list_filter = ['bill']

admin.site.register(models.Category)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.BillProducts, BillProductsAdmin)