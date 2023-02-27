from rest_framework import generics
from Products.serializers import ProductSerializer
from .models import Product


class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

