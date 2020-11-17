from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Product, Order, OrderItem, ShippingAddress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
