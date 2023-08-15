```python
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    product_number = models.CharField(max_length=50)
    vendor_name = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/')
    product_link = models.URLField()

    def __str__(self):
        return self.product_name
```