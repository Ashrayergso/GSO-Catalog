```python
from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Test Product', description='Test Description', product_number='123', vendor_name='Test Vendor', cost=100, product_image='test.jpg', product_site='www.test.com')

    def test_name_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, 'Test Product')

    def test_description_content(self):
        product = Product.objects.get(id=1)
        expected_object_description = f'{product.description}'
        self.assertEquals(expected_object_description, 'Test Description')

    def test_product_number_content(self):
        product = Product.objects.get(id=1)
        expected_object_product_number = f'{product.product_number}'
        self.assertEquals(expected_object_product_number, '123')

    def test_vendor_name_content(self):
        product = Product.objects.get(id=1)
        expected_object_vendor_name = f'{product.vendor_name}'
        self.assertEquals(expected_object_vendor_name, 'Test Vendor')

    def test_cost_content(self):
        product = Product.objects.get(id=1)
        expected_object_cost = f'{product.cost}'
        self.assertEquals(expected_object_cost, '100')

    def test_product_image_content(self):
        product = Product.objects.get(id=1)
        expected_object_product_image = f'{product.product_image}'
        self.assertEquals(expected_object_product_image, 'test.jpg')

    def test_product_site_content(self):
        product = Product.objects.get(id=1)
        expected_object_product_site = f'{product.product_site}'
        self.assertEquals(expected_object_product_site, 'www.test.com')
```