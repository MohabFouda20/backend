from rest_framework import viewsets
from .models import Product
from .serializers import productSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'