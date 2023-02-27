from rest_framework import generics
from Products.serializers import ProductSerializer
from .models import Product
from . import views



class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
p_createView = ProductCreateApi.as_view()

class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

