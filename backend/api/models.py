from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class Customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')

    def __str__(self):
        return self.user.get_full_name()

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Clothes','Clothes'),
        ('Electronics','Electronics'),
        ('Home','Home'),
        ('Books','Books')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='Clothes')
    image = models.ImageField(upload_to='product_image', default='default_product.jpg', blank=True)
    rating = models.PositiveIntegerField(default=5, null=True, blank=True,validators=[MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # If true, then new items should be added in new order
    order_complete = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100)

    def __str__(self):
        return (self.customer.user.get_full_name() + ' ' + str(self.order_id))

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200, null=True)

    def __str__(self):
        return (self.customer.user.get_full_name() + ' ' + self.address)
