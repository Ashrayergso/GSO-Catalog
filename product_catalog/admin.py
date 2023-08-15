```python
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'product_number', 'vendor_name', 'cost', 'product_image', 'product_link')
    search_fields = ('name', 'product_number', 'vendor_name')

admin.site.register(Product, ProductAdmin)
```