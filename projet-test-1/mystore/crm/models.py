from django.db import models

class Customer(models.Model):
    fname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=30, default="customer@.com")
    status = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Product(models.Model):
    CATEGORY = (
        ('Electronic', 'Electronic'),
        ('Fashion', 'Fashion'),
        ('Food', 'Food'),
    )
    
    name = models.fields.CharField(max_length=50, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    category = models.fields.CharField(max_length=10, null=True, choices=CATEGORY)
    description = models.fields.TextField(max_length=200, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    # def __str__(self):
    #     return f"{self.customer} {self.product}"
