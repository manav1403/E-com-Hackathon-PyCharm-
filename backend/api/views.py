from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from .models import Customer, Product, Order, OrderItem, ShippingAddress
from .serializers import StoreSerializer, CartSerializer

class Store(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = StoreSerializer
    search_fields = ['name', 'category']
    filter_backends = (SearchFilter,)

